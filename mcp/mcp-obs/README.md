# MCP Observability Server

MCP server providing observability tools for querying VictoriaLogs and VictoriaTraces.

## Tools

- `logs_search` - Search logs using LogsQL queries
- `logs_error_count` - Count errors per service over a time window
- `traces_list` - List recent traces for a service
- `traces_get` - Fetch a specific trace by ID

## Usage

```bash
python -m mcp_obs.server
```

## Configuration

The server connects to:
- VictoriaLogs at `http://victorialogs:9428`
- VictoriaTraces at `http://victoriatraces:10428`

These URLs are configured for Docker Compose networking.
