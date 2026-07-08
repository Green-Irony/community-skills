# community-skills

Green Irony's public Claude skill library. Skills teach Claude how to perform
tasks in a repeatable way across Cowork and Claude Code sessions.

This repo is where Green Irony publishes skills for the community. It currently
ships **pipeline-companion**, the wingman for the
[My Pipeline / Sales Command Center](https://greenirony.com) Notion CRM template:
work your deals, prep calls, log activity, draft follow-ups, and track quota —
all through your own Notion connector.

## What's in this repo

- `skills/` — One directory per skill. Each contains a `SKILL.md` and a `README.md`.
- `spec/adr/` — Architecture Decision Records for this repo.
- `template/` — Starter template for authoring new skills.
- `tests/` — CI test fixtures, including the deliberate-failure fixture.
- `scripts/` — Validation and test scripts run by CI.

## Installing skills

```shell
/plugin marketplace add Green-Irony/community-skills
```

Or install a specific skill:

```shell
/plugin install pipeline-companion@community-skills
```

## Adding a new skill

1. Copy `template/SKILL.md` into a new directory under `skills/`.
2. Name the directory to match the `name` field in the frontmatter.
3. Add the skill to `.claude-plugin/marketplace.json`.
4. Open a PR — a CODEOWNERS-required architect review is mandatory.

## Contributing

Contributions are welcome via pull request. Every PR is validated by CI
(structure + schema checks and a deliberate-failure test) and requires review
from a Green Irony architect before merging. Please do not attempt to bypass
branch protection.

## License

Licensed under the [Apache License 2.0](LICENSE).
