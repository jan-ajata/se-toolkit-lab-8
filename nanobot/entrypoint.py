#!/usr/bin/env python3
"""
Entrypoint for nanobot Docker container.

Resolves environment variables into config.json at runtime, then launches nanobot gateway.
Docker passes config via env vars, not by editing files.
"""

import json
import os
import sys


def main():
    # Read the base config
    config_path = "/app/nanobot/config.json"
    resolved_path = "/tmp/config.resolved.json"
    workspace_path = "/app/nanobot/workspace"

    with open(config_path, "r") as f:
        config = json.load(f)

    # Inject LLM provider config from env vars
    llm_api_key = os.environ.get("LLM_API_KEY")
    llm_api_base_url = os.environ.get("LLM_API_BASE_URL")
    llm_api_model = os.environ.get("LLM_API_MODEL")

    if llm_api_key:
        config["providers"]["custom"]["apiKey"] = llm_api_key
    if llm_api_base_url:
        config["providers"]["custom"]["apiBase"] = llm_api_base_url
    if llm_api_model:
        config["agents"]["defaults"]["model"] = llm_api_model

    # Inject gateway config from env vars
    gateway_host = os.environ.get("NANOBOT_GATEWAY_CONTAINER_ADDRESS")
    gateway_port = os.environ.get("NANOBOT_GATEWAY_CONTAINER_PORT")

    if gateway_host:
        config["gateway"]["host"] = gateway_host
    if gateway_port:
        config["gateway"]["port"] = int(gateway_port)

    # Inject MCP LMS server config from env vars
    lms_backend_url = os.environ.get("NANOBOT_LMS_BACKEND_URL")
    lms_api_key = os.environ.get("NANOBOT_LMS_API_KEY")

    if lms_backend_url:
        config["tools"]["mcpServers"]["lms"]["env"]["NANOBOT_LMS_BACKEND_URL"] = (
            lms_backend_url
        )
    if lms_api_key:
        config["tools"]["mcpServers"]["lms"]["env"]["NANOBOT_LMS_API_KEY"] = lms_api_key

    # Inject webchat channel config if enabled via env vars
    # Note: The webchat channel plugin requires nanobot-webchat package (installed in Part B)
    webchat_host = os.environ.get("NANOBOT_WEBCHAT_CONTAINER_ADDRESS")
    webchat_port = os.environ.get("NANOBOT_WEBCHAT_CONTAINER_PORT")

    if webchat_host or webchat_port:
        if "webchat" not in config["channels"]:
            config["channels"]["webchat"] = {}
        config["channels"]["webchat"]["enabled"] = True
        config["channels"]["webchat"]["allowFrom"] = ["*"]
        if webchat_host:
            config["channels"]["webchat"]["host"] = webchat_host
        if webchat_port:
            config["channels"]["webchat"]["port"] = int(webchat_port)

    # Inject webchat MCP server config (Part B)
    # This enables the agent to send structured UI messages to the active web chat
    nanobot_access_key = os.environ.get("NANOBOT_ACCESS_KEY")
    gateway_port_val = config["gateway"]["port"]

    if nanobot_access_key:
        if "mcpServers" not in config["tools"]:
            config["tools"]["mcpServers"] = {}
        config["tools"]["mcpServers"]["webchat"] = {
            "command": "python",
            "args": ["-m", "mcp_webchat"],
            "env": {
                "NANOBOT_ACCESS_KEY": nanobot_access_key,
                "NANOBOT_UI_RELAY_URL": f"http://localhost:{gateway_port_val}",
                "NANOBOT_UI_RELAY_TOKEN": nanobot_access_key,
            },
        }

    # Inject MCP observability server config (Part C)
    # This enables the agent to query VictoriaLogs and VictoriaTraces
    if "mcpServers" not in config["tools"]:
        config["tools"]["mcpServers"] = {}
    config["tools"]["mcpServers"]["obs"] = {
        "command": "python",
        "args": ["-m", "mcp_obs.server"],
        "env": {},
    }

    # Write resolved config
    with open(resolved_path, "w") as f:
        json.dump(config, f, indent=2)

    print(f"Using config: {resolved_path}", file=sys.stderr)

    # Exec into nanobot gateway
    os.execvp("nanobot", ["nanobot", "gateway", "--config", resolved_path, "--workspace", workspace_path])


if __name__ == "__main__":
    main()
