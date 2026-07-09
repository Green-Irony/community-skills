# ADR-0002: Switch to per-plugin layout for community-skills

## Status

Accepted

## Context

[[ADR-0001]] chose the anthropics/skills flat layout (`skills/<name>/SKILL.md`)
so that skills could be promoted from the private cowork-skills intake repo
without restructuring. In practice, this flat layout is incompatible with how
Claude web resolves a marketplace: it expects each entry in
`.claude-plugin/marketplace.json` to point at a self-contained plugin
directory containing its own `skills/` subdirectory, matching the
anthropics/knowledge-work-plugins layout. With the flat layout, Claude web
could not add this repo as a marketplace at all — not a style tradeoff, a
functional blocker.

## Decision

Supersede ADR-0001. Adopt the per-plugin layout: each plugin lives under
`plugins/<plugin-name>/`, containing its own `.claude-plugin/plugin.json`,
`README.md`, and a `skills/` subdirectory with one skill per subdirectory
(each named to match its SKILL.md frontmatter `name` field). A plugin may
bundle more than one skill.

`.claude-plugin/marketplace.json` plugin `source` entries point at the
plugin root (e.g. `./plugins/pipeline-companion`), not at the skill
directory directly.

`scripts/validate_structure.py` is updated accordingly: for each plugin
source, it requires a `skills/` subdirectory containing at least one skill
directory, and validates SKILL.md frontmatter (`name`, `description`, and
name-matches-directory) against each skill directory rather than the plugin
root.

## Consequences

- Pro: Repo is installable as a Claude web / Claude Code marketplace, which
  the flat layout never supported.
- Pro: Matches anthropics/knowledge-work-plugins, and supports bundling
  multiple skills under one plugin later without another restructure.
- Con: Promotion from the private cowork-skills intake repo (flat layout) now
  requires nesting the skill under `plugins/<name>/skills/<name>/` and adding
  a `plugin.json`, rather than a straight directory copy.

## Alternatives considered

Keeping the flat layout and working around it in `marketplace.json` —
rejected because the constraint is on the Claude web marketplace resolver,
not on this repo's manifest; no manifest shape fixes it without the
per-plugin directories.
