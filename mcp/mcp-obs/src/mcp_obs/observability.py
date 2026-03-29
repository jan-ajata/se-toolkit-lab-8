"""
Observability MCP server for VictoriaLogs and VictoriaTraces.

Provides tools for:
- logs_search: Search logs by keyword and/or time range
- logs_error_count: Count errors per service over a time window
- traces_list: List recent traces for a service
- traces_get: Fetch a specific trace by ID
"""

import httpx
import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("mcp_obs")

# VictoriaLogs API endpoint - read from env var or use Docker default
VICTORIALOGS_URL = os.environ.get(
    "NANOBOT_VICTORIALOGS_URL",
    "http://victorialogs:9428"
)

# VictoriaTraces API endpoint - read from env var or use Docker default
VICTORIATRACES_URL = os.environ.get(
    "NANOBOT_VICTORIATRACES_URL",
    "http://victoriatraces:10428"
)


@mcp.tool()
async def logs_search(query: str = "_time:10m", limit: int = 20) -> list[dict]:
    """
    Search VictoriaLogs using LogsQL query.

    Args:
        query: LogsQL query string. Examples:
            - "_time:10m" - logs from last 10 minutes
            - "_time:1h service.name:"Learning Management Service"" - backend logs from last hour
            - "_time:1h severity:ERROR" - errors from last hour
            - "event:db_query" - database query events
        limit: Maximum number of log entries to return (default: 20)

    Returns:
        List of log entries as dictionaries with fields like:
        - _time: timestamp
        - _msg: log message
        - severity: log level (INFO, ERROR, etc.)
        - service.name: service identifier
        - event: event type
        - trace_id: associated trace ID if present
    """
    async with httpx.AsyncClient() as client:
        url = f"{VICTORIALOGS_URL}/select/logsql/query"
        params = {"query": query, "limit": limit}
        response = await client.get(url, params=params, timeout=30.0)
        response.raise_for_status()
        # VictoriaLogs returns JSON lines (newline-delimited JSON), parse each line
        import json
        lines = response.text.strip().split('\n')
        results = []
        for line in lines:
            if line.strip():
                try:
                    results.append(json.loads(line))
                except json.JSONDecodeError:
                    pass  # Skip malformed lines
        return results


@mcp.tool()
async def logs_error_count(
    time_window: str = "10m",
    service: str | None = None,
) -> list[dict]:
    """
    Count errors per service over a time window.

    Args:
        time_window: Time window for the query (e.g., "10m", "1h", "24h")
        service: Optional service name to filter by (e.g., "Learning Management Service")

    Returns:
        List of error counts grouped by service with fields:
        - service.name: service identifier
        - error_count: number of errors in the time window
    """
    query = f"_time:{time_window} severity:ERROR"
    if service:
        query += f' service.name:"{service}"'

    async with httpx.AsyncClient() as client:
        url = f"{VICTORIALOGS_URL}/select/logsql/query"
        params = {"query": query, "limit": 1000}
        response = await client.get(url, params=params, timeout=30.0)
        response.raise_for_status()
        # Parse JSON lines response
        import json
        lines = response.text.strip().split('\n')
        logs = []
        for line in lines:
            if line.strip():
                try:
                    logs.append(json.loads(line))
                except json.JSONDecodeError:
                    pass

    # Count errors by service
    error_counts: dict[str, int] = {}
    for log in logs:
        service_name = log.get("service.name", "unknown")
        error_counts[service_name] = error_counts.get(service_name, 0) + 1

    return [
        {"service.name": name, "error_count": count}
        for name, count in sorted(error_counts.items(), key=lambda x: -x[1])
    ]


@mcp.tool()
async def traces_list(service: str = "Learning Management Service", limit: int = 10) -> list[dict]:
    """
    List recent traces for a service from VictoriaTraces.

    Args:
        service: Service name to filter traces (default: "Learning Management Service")
        limit: Maximum number of traces to return (default: 10)

    Returns:
        List of trace summaries with fields:
        - traceID: unique trace identifier
        - spans: number of spans in the trace
        - startTime: trace start time
        - duration: trace duration in microseconds
        - error: whether the trace contains errors
    """
    async with httpx.AsyncClient() as client:
        url = f"{VICTORIATRACES_URL}/select/jaeger/api/traces"
        params = {"service": service, "limit": limit}
        response = await client.get(url, params=params, timeout=30.0)
        response.raise_for_status()
        data = response.json()

    traces = data.get("data", [])
    result = []
    for trace in traces:
        spans = trace.get("spans", [])
        has_error = any(
            any(f.get("key") == "error" for log in span.get("logs", []))
            for span in spans
        )
        result.append({
            "traceID": trace.get("traceID"),
            "spans": len(spans),
            "startTime": spans[0].get("startTime") if spans else None,
            "duration": max((s.get("duration", 0) for s in spans), default=0),
            "error": has_error,
        })
    return result


@mcp.tool()
async def traces_get(trace_id: str) -> dict:
    """
    Fetch a specific trace by ID from VictoriaTraces.

    Args:
        trace_id: The trace ID to fetch (hex string, e.g., "6f9945811273ca3af6839f801b195774")

    Returns:
        Full trace data with:
        - traceID: trace identifier
        - spans: list of spans with operation names, tags, logs, and timing
        - processes: service information for each span
    """
    async with httpx.AsyncClient() as client:
        url = f"{VICTORIATRACES_URL}/select/jaeger/api/traces/{trace_id}"
        response = await client.get(url, timeout=30.0)
        response.raise_for_status()
        data = response.json()

    traces = data.get("data", [])
    if not traces:
        return {"error": f"Trace {trace_id} not found"}
    return traces[0]
