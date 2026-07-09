# plugins

Green Irony's public Claude Code plugin marketplace. One shelf for our free, community-facing
plugins across Cowork and Claude Code.

This repo currently ships **Notion CRM Companion**, the Claude-side companion for the
[My Pipeline / Sales Command Center](https://greenirony.com) Notion CRM template — its Pipeline
Tracker skill works your deals, preps calls, logs activity, drafts follow-ups, and tracks quota,
all through your own Notion connector.

## What's in this repo

- `plugins/` — One directory per plugin. Each contains a `.claude-plugin/plugin.json`, a
  `README.md`, and a `skills/` directory (one subdirectory per skill, each with a `SKILL.md`).
- `spec/adr/` — Architecture Decision Records for this repo.
- `template/` — Starter template for authoring new skills.
- `tests/` — CI test fixtures, including the deliberate-failure fixture.
- `scripts/` — Validation and test scripts run by CI.

## Installing plugins

```shell
/plugin marketplace add Green-Irony/plugins
```

Or install a specific plugin:

```shell
/plugin install notion-crm-companion@plugins
```

## Adding a new plugin

1. Copy `template/SKILL.md` into a new directory under `plugins/<plugin-name>/skills/<skill-name>/`.
2. Name the skill directory to match the `name` field in the frontmatter.
3. Add a `.claude-plugin/plugin.json` for the plugin, and register it in
   `.claude-plugin/marketplace.json`.
4. Open a PR — a CODEOWNERS-required architect review is mandatory.

## Contributing

Contributions are welcome via pull request. Every PR is validated by CI
(structure + schema checks and a deliberate-failure test) and requires review
from a Green Irony architect before merging. Please do not attempt to bypass
branch protection.

## License

Licensed under the [Apache License 2.0](LICENSE).
