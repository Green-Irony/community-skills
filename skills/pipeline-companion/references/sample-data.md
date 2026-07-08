# Template sample data

The records below ship with a freshly duplicated template. They are the same on every install,
so they're a reliable signal of an untouched pipeline the user hasn't loaded their real book into
yet. Use this to tell "sample data" apart from "real deals" during first-run setup (see the
"First run" section in SKILL.md).

Match by deal name. Users may rename or delete some, so treat a partial match as "likely still
samples" and confirm with one question rather than assuming.

## My Pipeline (free edition) — sample deals

- **Cascade Freight — Renewal + Expansion**
- **Brightline — Dispatch Automation Pilot**
- **Northwind — Ops Platform Rollout**

If the open pipeline is exactly (or mostly) these three, it's the shipped sample set — not the
user's book. Offer to import their real data. The connector has no delete verb, so you can't
remove the samples — deletion is the user's one manual step. Make it easy: after the import, hand
the user a direct Notion link to each sample deal (the live page URL from when you matched it) so
they can open and delete each one in a couple of clicks. Don't set them to Closed Lost or edit
them — just surface the links so real and sample deals don't stay mixed in the views.

If the pipeline contains these three **plus** other deals, the user has started adding real work —
don't treat it as an empty first run, and don't touch the samples unless the user asks.

## Full edition (Sales Command Center)

The full edition may ship with additional sample records across 🏢 Accounts, 💰 Quotes, and
🎯 Targets, and possibly its own sample deals. Those aren't catalogued here yet — if you're on the
full edition and see records that look like demo data, confirm with the user before acting on them.
