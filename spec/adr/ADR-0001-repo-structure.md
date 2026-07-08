# ADR-0001: Use anthropics/skills flat layout for community-skills

## Status

Accepted

## Context

Green Irony needed a public, community-facing repo to distribute Claude skills —
starting with pipeline-companion, the companion to the My Pipeline / Sales
Command Center Notion CRM template. It is a sibling to the private cowork-skills
repo, which serves as the internal intake and cleaning staging area; skills are
promoted here only after review. Two upstream layouts exist: the flat skills
layout (anthropics/skills, all skills under a top-level skills/ directory) and
the per-plugin layout (anthropics/knowledge-work-plugins, each plugin a
top-level directory with skills/ nested inside).

## Decision

Use the anthropics/skills flat layout: all skills live under skills/, one
subdirectory per skill, each named to match its SKILL.md frontmatter name field.
This mirrors the private cowork-skills repo so skills can be promoted between the
two without restructuring.

## Consequences

- Pro: Directory names match anthropics/skills and the private cowork-skills repo
  exactly — promotion from intake to public is a straight copy.
- Pro: Simpler — no plugin.json per skill, no commands/ or agents/ directories needed.
- Con: If Green Irony later wants per-role plugins, a migration will be required.

## Alternatives considered

anthropics/knowledge-work-plugins per-plugin layout — rejected because the
current public skill set has no role-based structure and the additional nesting
adds complexity without benefit.
