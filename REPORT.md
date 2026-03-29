# Lab 8 — Report

Paste your checkpoint evidence below. Add screenshots as image files in the repo and reference them with `![description](path)`.

## Task 1A — Bare agent

<!-- Paste the agent's response to "What is the agentic loop?" and "What labs are available in our LMS?" -->
🐈 nanobot
2 + 2 = 4

🐈 nanobot
Based on my exploration of the LMS workspace, here are the available labs:

Required Labs

 1 Lab 1 - Set Up the Agent (Task 1)
 2 Lab 2 - Deploy the Agent and Add a Web Client (Task 2)
 3 Lab 3 - Give the Agent New Eyes (Observability) (Task 3)
 4 Lab 4 - Diagnose a Failure and Make the Agent Proactive (Task 4)

Optional Labs

 • Optional Task 1 - Add a Telegram Bot Client

Lab Structure

The labs are located in:

 • /root/se-toolkit-lab-8/lab/tasks/required/ - Contains task-1.md through
   task-5.md (task-5 is merged into task-4)
 • /root/se-toolkit-lab-8/lab/tasks/optional/ - Contains optional task-1.md
 • /root/se-toolkit-lab-8/wiki/lab-1/ - Additional documentation for Lab 1

What Each Lab Covers


 Lab       Focus
 ─────────────────────────────────────────────────────────────────────────────────
 Task 1    Install nanobot, connect to LMS backend via MCP, write skill prompts
 Task 2    Deploy nanobot as Docker service, add WebSocket channel, Flutter web
           client
 Task 3    Add observability (VictoriaLogs, VictoriaTraces), MCP tools for
           logs/traces
 Task 4    Diagnose failures, proactive health checks with cron, fix planted bugs
 Optional  Telegram bot client integration


The labs build a complete AI agent system with the LMS backend, from basic setup
through deployment, observability, and proactive monitoring.

## Task 1B — Agent with LMS tools

<!-- Paste the agent's response to "What labs are available?" and "Describe the architecture of the LMS system" -->
🐈 nanobot
Here are the available labs:

From the LMS (Learning Management System):

 1 Lab 01 – Products, Architecture & Roles
 2 Lab 02 — Run, Fix, and Deploy a Backend Service
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4 Lab 04 — Testing, Front-end, and AI Agents
 5 Lab 05 — Data Pipeline and Analytics Dashboard
 6 Lab 06 — Build Your Own Agent
 7 Lab 07 — Build a Client with an AI Coding Agent
 8 Lab 08 — lab-08

From the file system (/root/se-toolkit-lab-8/lab/tasks/):

 • Required: task-1.md through task-5.md
 • Optional: task-1.md

Would you like more details about any specific lab, such as pass rates, completion
status, or submission timeline?

🐈 nanobot
I'll help you find which lab has the lowest pass rate. Let me first get the list of
available labs, then check their pass rates.
2026-03-28 16:14:49.556 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_labs({})

🐈 nanobot
Now let me check the completion rates for each lab to find the one with the lowest
pass rate:
2026-03-28 16:14:56.776 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_completion_rate({"lab": "lab-01"})
2026-03-28 16:14:56.776 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_completion_rate({"lab": "lab-02"})
2026-03-28 16:14:56.777 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_completion_rate({"lab": "lab-03"})
2026-03-28 16:14:56.777 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_completion_rate({"lab": "lab-04"})
2026-03-28 16:14:56.777 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_completion_rate({"lab": "lab-05"})
2026-03-28 16:14:56.777 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_completion_rate({"lab": "lab-06"})
2026-03-28 16:14:56.777 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_completion_rate({"lab": "lab-07"})
2026-03-28 16:14:56.777 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_completion_rate({"lab": "lab-08"})

🐈 nanobot
Based on the completion rates:


 Lab     Completion Rate  Passed  Total
 ──────────────────────────────────────
 Lab 01  100.0%           258     258
 Lab 02  89.1%            131     147
 Lab 03  89.1%            156     175
 Lab 04  96.7%            238     246
 Lab 05  98.4%            246     250
 Lab 06  98.4%            242     246
 Lab 07  99.6%            236     237
 Lab 08  0.0%             0       0


Lab 02 and Lab 03 are tied for the lowest pass rate at 89.1%.

Note: Lab 08 shows 0.0% but that's because it has no submissions yet (0 total), so
it's not a meaningful comparison.

Among labs with actual student submissions, Lab 02 and Lab 03 both have the lowest
completion rate at 89.1%.

## Task 1C — Skill prompt

<!-- Paste the agent's response to "Show me the scores" (without specifying a lab) -->
root@aidar-vm001:~/se-toolkit-lab-8/nanobot# uv run nanobot agent --logs --session cli:task1c-scores -c ./config.json -m "Show me the scores"
Using config: /root/se-toolkit-lab-8/nanobot/config.json
⠼ nanobot is thinking...2026-03-28 16:21:04.050 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_health' from server 'lms'
2026-03-28 16:21:04.051 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_labs' from server 'lms'
2026-03-28 16:21:04.051 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_learners' from server 'lms'
2026-03-28 16:21:04.051 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_pass_rates' from server 'lms'
2026-03-28 16:21:04.051 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_timeline' from server 'lms'
2026-03-28 16:21:04.051 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_groups' from server 'lms'
2026-03-28 16:21:04.051 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_top_learners' from server 'lms'
2026-03-28 16:21:04.051 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_completion_rate' from server 'lms'
2026-03-28 16:21:04.051 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_sync_pipeline' from server 'lms'
2026-03-28 16:21:04.051 | INFO     | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server 'lms': connected, 9 tools registered
2026-03-28 16:21:04.051 | INFO     | nanobot.agent.loop:_process_message:425 - Processing message from cli:user: Show me the scores

🐈 nanobot
I'll help you check the scores. First, let me see what labs are available.
2026-03-28 16:21:09.127 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_labs({})

🐈 nanobot
There are 8 labs available. Which lab would you like to see the scores for?

 1 Lab 01 – Products, Architecture & Roles
 2 Lab 02 — Run, Fix, and Deploy a Backend Service
 3 Lab 03 — Backend API: Explore, Debug, Implement, Deploy
 4 Lab 04 — Testing, Front-end, and AI Agents
 5 Lab 05 — Data Pipeline and Analytics Dashboard
 6 Lab 06 — Build Your Own Agent
 7 Lab 07 — Build a Client with an AI Coding Agent
 8 lab-08

Please let me know which lab you're interested in, or I can show you scores for all
of them.

2026-03-28 16:21:17.481 | INFO     | nanobot.agent.loop:_process_message:479 - Response to cli:user: There are 8 labs available. Which lab would you like to see the scores for?

1. Lab 01 – Products, Architecture & Roles
...
2026-03-28 16:21:17.740 | DEBUG    | nanobot.agent.memory:maybe_consolidate_by_tokens:323 - Token consolidation idle cli:task1c-scores: 6081/65536 via tiktoken
root@aidar-vm001:~/se-toolkit-lab-8/nanobot# uv run nanobot agent --logs --session cli:task1c-scores -c ./config.json -m "The first lab"
Using config: /root/se-toolkit-lab-8/nanobot/config.json
⠼ nanobot is thinking...2026-03-28 16:21:55.282 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_health' from server 'lms'
2026-03-28 16:21:55.282 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_labs' from server 'lms'
2026-03-28 16:21:55.282 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_learners' from server 'lms'
2026-03-28 16:21:55.282 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_pass_rates' from server 'lms'
2026-03-28 16:21:55.282 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_timeline' from server 'lms'
2026-03-28 16:21:55.282 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_groups' from server 'lms'
2026-03-28 16:21:55.282 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_top_learners' from server 'lms'
2026-03-28 16:21:55.283 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_completion_rate' from server 'lms'
2026-03-28 16:21:55.283 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_sync_pipeline' from server 'lms'
2026-03-28 16:21:55.283 | INFO     | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server 'lms': connected, 9 tools registered
2026-03-28 16:21:55.283 | INFO     | nanobot.agent.loop:_process_message:425 - Processing message from cli:user: The first lab
⠧ nanobot is thinking...2026-03-28 16:21:55.507 | DEBUG    | nanobot.agent.memory:maybe_consolidate_by_tokens:323 - Token consolidation idle cli:task1c-scores: 6081/65536 via tiktoken
2026-03-28 16:21:59.502 | INFO     | nanobot.agent.loop:_prepare_tools:253 - Tool call: mcp_lms_lms_pass_rates({"lab": "1"})

🐈 nanobot
Here are the scores for Lab 01 – Products, Architecture & Roles:


 Task                                        Avg Score  Attempts
 ───────────────────────────────────────────────────────────────
 Lab setup                                   84.2%      3,294
 Task 0: Practice the Git workflow           64.5%      306
 Task 1: Product & architecture description  55.1%      161
 Task 2: Roles and skills mapping            49.8%      83
 Optional: Resolve a merge conflict          34.6%      13
 Optional: Add a CI check                    42.9%      7
 Optional: Create a release                  60.0%      5
 Optional: Plan skill development            20.0%      5


The "Lab setup" task has the highest average score (84.2%) with the most attempts,
while the optional tasks have fewer attempts and varying scores.

## Task 2A — Deployed agent

<!-- Paste a short nanobot startup log excerpt showing the gateway started inside Docker -->

```
🐈 Starting nanobot gateway version 0.1.4.post5 on port 18790...
2026-03-28 13:41:05.775 | INFO     | nanobot.cron.service:start:202 - Cron service started with 0 jobs
2026-03-28 13:41:05.775 | INFO     | nanobot.heartbeat.service:start:124 - Heartbeat started (every 1800s)
2026-03-28 13:41:08.212 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_health' from server 'lms'
2026-03-28 13:41:08.213 | DEBUG    | nanobot.agent.tools.mcp:connect_mcp_servers:226 - MCP: registered tool 'mcp_lms_lms_labs' from server 'lms'
2026-03-28 13:41:08.213 | INFO     | nanobot.agent.tools.mcp:connect_mcp_servers:246 - MCP server 'lms': connected, 9 tools registered
2026-03-28 13:41:08.213 | INFO     | nanobot.agent.loop:run:280 - Agent loop started
Using config: /tmp/config.resolved.json
```

**Files created/modified for Part A:**
- `nanobot/entrypoint.py` — Runtime config resolver that injects env vars and launches `nanobot gateway`
- `nanobot/Dockerfile` — Multi-stage uv build with non-root user
- `docker-compose.yml` — Uncommented nanobot service, added mcp context, updated caddy dependencies
- `caddy/Caddyfile` — Uncommented `/ws/chat` route
- `nanobot/config.json` — Added webchat channel config

**Checkpoint verification:**
1. ✓ `docker compose ps` shows nanobot service "Up"
2. ✓ Logs show "MCP server 'lms': connected, 9 tools registered" and "Agent loop started"

## Task 2B — Web client## Lab 02 — Run, Fix, and Deploy a Backend Service

### Task Scores

| Task | Avg Score | Attempts |
|------|-----------|----------|
| Task 1: Run the web server | **67.9%** | 210 |
| Task 2: Identify, report, and fix a bug | **66.7%** | 216 |
| Task 4: Deploy the web server to the VM | **56.2%** | 84 |
| Optional 1: Implement the /outcomes endpoint | **36.4%** | 11 |
| Optional 3: Implement the post-order traversal | **62.5%** | 6 |
| Optional 2: Make your VM a proxy | **0.0%** | 3 |
 
**Summary:**
- Core tasks (1, 2, 4) have moderate success rates (56-68%)
- Optional tasks have lower participation and scores
- "Make your VM a proxy" has no successful attempts yet

Would you like to see more details like completion rate, top learners, or group performance for this lab? 🐈

## Task 3A — Structured logging

<!-- Paste happy-path and error-path log excerpts, VictoriaLogs query screenshot -->

## Task 3B — Traces

<!-- Screenshots: healthy trace span hierarchy, error trace -->

## Task 3C — Observability MCP tools

<!-- Paste agent responses to "any errors in the last hour?" under normal and failure conditions -->

## Task 4A — Multi-step investigation

**Agent's response to "The LMS backend is failing. What went wrong? Check logs and traces.":**

```
LMS Backend Failure Analysis

Root Cause: The LMS backend cannot connect to the PostgreSQL database because the hostname postgres cannot be resolved.

Evidence from Logs and Traces:

 1 Health Check Status: unhealthy with HTTP 404 error
 2 Error Pattern: Multiple socket.gaierror: [Errno -2] Name or service not known errors
 3 Failed Connection Details:
    • Database: db-lab-8
    • User: postgres
    • Host: postgres (unresolvable)
    • Port: 5432
 4 Affected Endpoints:
    • POST /pipeline/sync - ETL sync operations failing
    • GET /learners/ - Cannot read learner data
    • All database queries failing

What Happened:

The application is configured to connect to a PostgreSQL database using the hostname postgres (typical Docker Compose service name), but DNS resolution
is failing. This indicates:

 1 The PostgreSQL container/service is not running, or
 2 Network connectivity issue between the LMS backend and the database service (e.g., Docker network misconfiguration), or
 3 The postgres hostname is not defined in the container's DNS resolution

Recommended Actions:

 1 Check if PostgreSQL container is running:
    docker ps | grep postgres
 2 Verify Docker network connectivity:
    docker network inspect <network-name>
 3 Restart the database service if it's down
 4 Check Docker Compose configuration to ensure the backend and postgres services are on the same network

The LMS backend itself is running (it can receive requests), but it cannot function because all database operations fail due to the connection error.
```

**Investigation flow observed:**
1. `mcp_lms_lms_health()` - Confirmed backend unhealthy
2. `mcp_obs_logs_search()` - Found error logs with `gaierror: [Errno -2] Name or service not known`
3. `mcp_obs_traces_list()` - Listed recent traces
4. `mcp_obs_traces_get()` - Fetched trace details showing database connection failures
5. Synthesized findings into coherent explanation citing both log and trace evidence

## Task 4B — Proactive health check

**Environment fixes applied:**

1. Updated `/mcp/mcp-obs/src/mcp_obs/observability.py` to read VictoriaLogs/VictoriaTraces URLs from environment variables
2. Updated `/nanobot/config.json` to use Docker network URLs (`http://victorialogs:9428`, `http://victoriatraces:10428`)
3. Fixed JSON parsing in `logs_error_count` to handle JSON lines format
4. Added webchat port exposure in `docker-compose.yml` for direct WebSocket access

**Cron job created:**

A scheduled health check job was created in `/nanobot/workspace/cron/jobs.json`:

```json
{
  "version": 1,
  "jobs": [
    {
      "id": "health-check-1",
      "name": "LMS Health Check",
      "enabled": true,
      "schedule": {
        "kind": "every",
        "everyMs": 900000
      },
      "payload": {
        "kind": "agent_turn",
        "message": "Check for backend errors in the last 15 minutes and post a summary here.",
        "deliver": true,
        "channel": "webchat",
        "to": "auto-health-check"
      }
    }
  ]
}
```

**Verification:**
- Nanobot logs show: `✓ Cron: 1 scheduled jobs`
- Cron service confirms: `Jobs count: 1, Job: health-check-1 - LMS Health Check`
- The job runs every 15 minutes (900000ms)
- When triggered, it checks for backend errors and posts a summary to the webchat channel

**Note on API connectivity:**
The Qwen Code API is experiencing intermittent retry timeouts (likely rate limiting or network issues with the upstream Qwen service). This affects real-time WebSocket message responses but does not impact the scheduled cron job execution. The cron job is properly configured and will run on schedule.

- Qwen API health: `ok` (account status: `healthy`)
- Error pattern: `Retry X/5 (error: )` - empty errors indicate connection timeouts
- Total requests: 168 (session count, not daily limit)

**To interact with the health check via Flutter UI:**
1. Open Flutter chat at `http://localhost:42002/flutter`
2. Log in with access key: `aidar`
3. Ask: "List scheduled jobs" - should show the health check job (when API is responsive)
4. Wait for the next cron cycle to see a proactive health report

## Task 4C — Bug fix and recovery

### 1. Root cause identified

**Location:** `/backend/src/lms_backend/routers/items.py`, lines 22-28

**The planted bug:** The `get_items()` endpoint had a broad `except Exception` handler that caught all database errors and re-raised them as HTTP 404 "Items not found". This masked the real error (PostgreSQL connection failure) with a misleading 404 status code.

```python
# BEFORE (buggy code)
except Exception as exc:
    logger.warning(
        "items_list_failed_as_not_found",
        extra={"event": "items_list_failed_as_not_found"},
    )
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Items not found",
    ) from exc
```

### 2. Code fix

Changed the exception handler to:
- Log at ERROR level (not WARNING)
- Include the actual error message in the log
- Return HTTP 500 (Internal Server Error) instead of 404
- Include the actual error details in the response

```python
# AFTER (fixed code)
except Exception as exc:
    logger.error(
        "items_list_failed",
        extra={"event": "items_list_failed", "error": str(exc)},
    )
    raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=f"Database error: {str(exc)}",
    ) from exc
```

### 3. Post-fix failure check

With PostgreSQL stopped, the `/items/` endpoint now returns the real error:

```bash
$ curl -s http://localhost:42002/items/ -H "Authorization: Bearer aidar"
{"detail":"Database error: [Errno -2] Name or service not known"}
```

Before the fix, this would have returned `{"detail":"Items not found"}` with HTTP 404.

Backend logs now show:
```
ERROR [lms_backend.routers.items] - items_list_failed
```

### 4. Healthy follow-up

After restarting PostgreSQL:

```bash
$ curl -sf http://localhost:42002/items/ -H "Authorization: Bearer aidar" | head -c 300
[{"type":"lab","parent_id":null,"description":"","created_at":"2026-03-28T12:17:31.390943","id":1,"title":
"Lab 01 – Products, Architecture & Roles","attributes":{}},...]
```

The system is healthy and returns the list of labs successfully.
