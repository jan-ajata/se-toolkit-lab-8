---
name: lms
description: Use LMS MCP tools for live course data
always: true
---

# LMS Skill

Use LMS MCP tools to answer questions about labs, learners, and performance metrics.

## Available Tools

- `lms_health` — Check if the LMS backend is healthy and get the item count. No arguments.
- `lms_labs` — List all labs available in the LMS. No arguments.
- `lms_learners` — List all learners registered in the LMS. No arguments.
- `lms_pass_rates` — Get pass rates (avg score and attempt count per task) for a lab. Requires `lab`.
- `lms_timeline` — Get submission timeline (date + submission count) for a lab. Requires `lab`.
- `lms_groups` — Get group performance (avg score + student count per group) for a lab. Requires `lab`.
- `lms_top_learners` — Get top learners by average score for a lab. Requires `lab`, optional `limit` (default 5).
- `lms_completion_rate` — Get completion rate (passed / total) for a lab. Requires `lab`.
- `lms_sync_pipeline` — Trigger the LMS sync pipeline. Use when data seems stale.

## Strategy

### When the user asks about scores, pass rates, completion, groups, timeline, or top learners

1. If the user did not specify a lab, call `lms_labs` first to get available labs.
2. If multiple labs are available, use the `structured-ui` skill to ask the user to choose one.
   - Use each lab's `title` field as the label.
   - Use each lab's `id` field as the value to pass back.
3. Once a lab is selected, call the appropriate tool (`lms_pass_rates`, `lms_completion_rate`, etc.).

### When the user asks "what labs are available" or "what can you do"

- Call `lms_labs` and list the lab titles.
- Explain that you can provide pass rates, completion rates, timelines, group performance, and top learners for any lab.

### Formatting results

- Format percentages with one decimal place (e.g., "75.3%").
- Show counts as integers.
- Keep responses concise — lead with the answer, then add brief context if helpful.
- When showing top learners, include their names and average scores.

### Example flow for "Show me the scores"

1. Call `lms_labs` to get available labs.
2. If multiple labs exist, present a choice using `structured-ui` with lab titles as labels.
3. After the user picks a lab, call `lms_pass_rates` with that lab ID.
4. Format and present the results.
