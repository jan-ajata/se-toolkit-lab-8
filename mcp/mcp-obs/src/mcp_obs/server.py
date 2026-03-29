"""
MCP Observability Server entry point.

Run with: python -m mcp_obs.server
"""

from mcp_obs.observability import mcp

if __name__ == "__main__":
    mcp.run()
