# pipeline-companion

Companion for Green Irony's My Pipeline / Sales Command Center Notion CRM templates — runs the
rep's admin: import, call prep, logging call notes, follow-up emails, quota, and pipeline reviews.
The rep talks; the skill does the Notion busywork.

## Prerequisites

- The **My Pipeline** or **Sales Command Center** Notion template installed (duplicated) in your
  workspace. The skill finds it by the "🚀 Start Here" page — it can't install it for you.
- The **Notion connector** authorized in Claude. The skill works entirely through your own Notion
  workspace and touches no other services.

## Quick start

Not sure where to begin? Just ask: **"how do I get started managing my pipeline"** and the skill
will walk you through it. Or do it directly:

## Commands

- **import my book** — first-run data load from a CSV, paste, or memory
- **new deal** — add a single new opportunity to the pipeline
- **prep [name]** — pre-call brief on a deal
- **log a call** — capture notes/transcript into the deal's log and update its fields
- **follow up** — draft the recap email from the last logged activity
- **menu** — list what's available

Full edition (Sales Command Center) adds: **brief**, **review**, **quota**, **history [account]**,
and **crm update**. On the free My Pipeline edition these degrade gracefully — the skill does the
best honest version with what's available and names the capability gap once.

## Source

Green Irony original. Built for the My Pipeline / Sales Command Center Notion templates by
Green Irony. Operates entirely through the user's own Notion connector — no other services.
