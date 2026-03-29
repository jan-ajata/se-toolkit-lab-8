# Observability Skill

You have access to observability tools that can query VictoriaLogs and VictoriaTraces. Use these tools to investigate system health, errors, and request traces.

## Available Tools

### Log Tools (VictoriaLogs)

- **logs_search(query, limit)** - Search logs using LogsQL queries
  - Example queries:
    - `"_time:10m"` - logs from last 10 minutes
    - `"_time:1h service.name:\"Learning Management Service\""` - backend logs from last hour
    - `"_time:1h severity:ERROR"` - errors from last hour
    - `"event:db_query"` - database query events
  - Returns list of log entries with fields: `_time`, `_msg`, `severity`, `service.name`, `event`, `trace_id`

- **logs_error_count(time_window, service)** - Count errors per service
  - `time_window`: e.g., "10m", "1h", "24h"
  - `service`: optional filter, e.g., "Learning Management Service"
  - Returns list of `{service.name, error_count}` sorted by count

### Trace Tools (VictoriaTraces)

- **traces_list(service, limit)** - List recent traces for a service
  - Returns trace summaries with: `traceID`, `spans`, `startTime`, `duration`, `error`

- **traces_get(trace_id)** - Fetch full trace details
  - Returns complete trace with all spans, tags, and logs

## One-Shot Investigation Protocol

When the user asks **"What went wrong?"** or **"Check system health"**, follow this exact flow in a single pass:

1. **Check error count first** — Call `logs_error_count(time_window="10m")` to see which services have recent errors
   - This tells you immediately if there are any errors and which service is affected

2. **Search for error details** — Call `logs_search(query="_time:10m severity:ERROR", limit=10)`
   - Look for the most recent error entries
   - Extract any `trace_id` from the log entries
   - Note the `service.name`, `event`, and error message

3. **Fetch the trace** — If you found a `trace_id`, call `traces_get(trace_id)` immediately
   - This shows the full request flow across services
   - Identify which span has `error: true`
   - Look at the span's logs for the actual exception or failure reason

4. **Synthesize the answer** — Combine log evidence and trace evidence into one coherent explanation:
   - **What failed**: the service name and operation
   - **Why it failed**: the actual error message from logs/traces (e.g., "PostgreSQL connection refused", "SQLAlchemy OperationalError")
   - **Evidence**: cite both the log entry and the trace span that show the failure
   - **Impact**: what user-facing functionality is broken (e.g., "cannot list labs", "API returns 500")

### Critical: Look for the real error, not the symptom

When investigating failures, pay attention to what the logs and traces actually show:

- If logs show `db_query` with an error like "connection refused" or "can't connect to PostgreSQL", that's the **root cause**
- If the HTTP response status is `404` but the trace shows a database failure, the `404` is **misleading** — the real issue is the database being down
- Always trace back to the **first failing span** in the trace — that's where the real error originated

## Reasoning Flow

When the user asks about errors or system health:

1. **Start with logs_error_count** - Get a quick overview of recent errors
   - Use a narrow time window like "10m" for fresh data
   - Filter by service if the user asks about a specific service

2. **Use logs_search for details** - Inspect the actual error messages
   - Query: `"_time:10m severity:ERROR service.name:\"Learning Management Service\""`
   - Look for `trace_id` in the log entries

3. **Fetch the trace if needed** - Use `traces_get(trace_id)` to see the full request flow
   - Identify which span failed
   - Check the error message and stack trace in span logs

4. **Summarize findings** - Provide a concise answer
   - Don't dump raw JSON
   - Explain what went wrong in plain language
   - Mention the affected service and operation

## Example Queries

**"Any errors in the last 10 minutes?"**
```
1. logs_error_count(time_window="10m")
2. If errors found: logs_search(query="_time:10m severity:ERROR", limit=10)
3. Summarize: which services have errors, what the errors are
```

**"What went wrong?"** (investigation flow)
```
1. logs_error_count(time_window="10m") — see which services have errors
2. logs_search(query="_time:10m severity:ERROR", limit=10) — get error details
3. Extract trace_id from the most recent error log
4. traces_get(trace_id) — fetch the full trace
5. Synthesize: "The LMS backend failed because [root cause from trace]. 
   Logs show [error message] at [timestamp]. 
   The trace shows the request failed at [span name] with [specific error].
   This caused [user-facing impact]."
```

**"What's wrong with the LMS backend?"**
```
1. logs_error_count(time_window="10m", service="Learning Management Service")
2. logs_search(query="_time:10m service.name:\"Learning Management Service\" severity:ERROR")
3. If trace_id found: traces_get(trace_id)
4. Explain the failure chain
```

**"Show me recent request traces"**
```
1. traces_list(service="Learning Management Service", limit=5)
2. For interesting traces: traces_get(trace_id)
3. Show the span hierarchy and timing
```

## Tips

- Always use scoped time windows like "10m" or "1h" to avoid historical noise
- Focus on the LMS backend when asked about "the system" - that's the primary service
- Extract `trace_id` from logs to correlate logs with traces
- When you find an error trace, look at the span with `error: true` to find the root cause
- **For database failures**: if PostgreSQL is down, you'll see connection errors in logs and the first failing span will be the database query
- **Don't be misled by HTTP status codes** — a 404 response might actually be a 500 error hidden by poor exception handling
