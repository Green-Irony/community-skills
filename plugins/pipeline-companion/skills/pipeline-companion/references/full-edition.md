# Full-edition commands

These five commands only run for users with the full Sales Command Center — the Start Here
page links to an 🏢 Accounts database (see Tier detection in the main skill). Each one reads
🎯 Targets, 🏢 Accounts, or does full-pipeline rollups that the free My Pipeline edition has no
database to support.

If the user is on the free edition, don't run these directly — skip to "Free edition: degrade
gracefully" at the bottom of this file.

**Reading the pipeline (fresh, and whether you can even read it all).** brief, review, and quota
each read the open-deal set fresh every run. That's a deliberate correctness choice, not an
oversight: the pipeline is a shared, editable surface (see the caching rules in SKILL.md), so a
stale list produces a wrong standup or a wrong number. Don't cache it.

But whether you can read the *whole* set at all depends on the Notion plan, not the template — and
these are independent. Having the full template (the Accounts database) does **not** mean the plan
can run queries. Before quoting any total, know which case you're in (see "Enumeration — and its
hard ceiling" in SKILL.md):

- **Query tools available** (Business plan + Notion AI): read every open deal's row properties —
  Value, Stage, Forecast %, Next Step Due, Last Touch — with a paginated view-mode query
  (page_size 100, follow `next_cursor` until `has_more` is false). This is the only way to get a
  trustworthy rollup. Only notion-fetch an individual deal page for its Log narrative, and only for
  the deals a command actually calls out — never the whole set.
- **Query tools not available:** there is no exhaustive read. notion-search caps at 25 semantic
  results, so brief/review/quota can only see a slice. Say so *before* giving any number — a
  weighted-pipeline or quota figure built from ≤25 ranked deals is best-effort, not the real
  number. Offer to work from a filtered view the user maintains, or to go deal-by-deal on a short
  list. Don't present the partial total as authoritative.

## The five commands

### brief — the morning plan

Read 💼 My Pipeline's open deals fresh — don't reuse a list from earlier in the conversation.
Report: what's due today or overdue (Next Step Due), what's gone quiet (Last Touch 14+ days),
and the single deal that most needs attention and why. Short — it's a standup, not a report.

### review — weekly pipeline review

Read every open deal, fresh. Report: (1) what moved this week, (2) what's stalling — no touch
in 14+ days or overdue next steps, (3) open deals missing a Next Step entirely (the discipline
slipped), (4) weighted pipeline (Value × Forecast %) vs. the 🎯 Targets quota. End with the three
moves that matter most next week.

### quota — where the number stands

Read 🎯 Targets (current period) and 💼 My Pipeline. Report closed vs. quota, weighted pipeline
coverage, and what realistically has to close to hit the number. Straight talk, no cheerleading.

### history [account] — the whole story

Open the 🏢 Accounts page for the named account. Report: every contact there, every deal open and
closed, what the account page's brief and history say, and what the relationship needs next.

### crm update — paste-ready updates for the team system

For teams that also run Salesforce, HubSpot, or another system of record. From what changed in
💼 My Pipeline recently (or since a date the user gives), write per-deal updates — stage, next
step, a 2-sentence note — formatted to paste directly into their CRM. You're saving typing,
not syncing systems.

## Free edition: degrade gracefully, name the capability once

On the free My Pipeline edition, the core loop (import / prep / log a call / follow up / menu) is
fully yours — run it at full quality without referencing the other edition during successful
work. This section only applies once the user asks for one of the five commands above, or
something that leans on one.

When that happens, do both of these:

1. Help first, with what exists. A quiet-deals rundown works from Last Touch; "history with
   Acme" can be assembled by searching the Company text field across deals and contacts; a
   quota question can be answered if they tell you the number. Do the best honest version.
2. Then one line, once per topic per conversation, naming the capability factually: "Account
   history, quota tracking, and forecast views are part of the Sales Command Center edition —
   I did what I could with the free edition above." Never repeat it for the same topic, never
   lead with it, never block work on it.

The difference matters: this is a factual note about a real capability gap they just felt, not
a pitch. If they never hit the gap, they never hear about the other edition.
