"""
validate_structure.py — Validates the plugins repo structure.

Layout (ADR-0002): each marketplace plugin's source directory must contain a
skills/ subdirectory with one directory per bundled skill, each holding a
SKILL.md whose frontmatter name matches the skill directory name.

Usage:
    python scripts/validate_structure.py
    python scripts/validate_structure.py --manifest /path/to/test-marketplace.json

The --manifest argument overrides the default .claude-plugin/marketplace.json
path. Used by test_deliberate_failure.py to run the validator against a
synthetic manifest without touching real files.

Path resolution: all paths (schema, default manifest, source directories)
are resolved relative to the script file's own location using pathlib:
    REPO_ROOT = Path(__file__).parent.parent.resolve()
This means the script produces consistent results regardless of the working
directory from which it is invoked.

Exit codes:
    0 — All checks passed.
    1 — One or more checks failed (error messages printed to stdout).
"""

import argparse
import json
import sys
from pathlib import Path

import frontmatter
import jsonschema

REPO_ROOT = Path(__file__).parent.parent.resolve()


def main():
    parser = argparse.ArgumentParser(description="Validate plugins repo structure.")
    parser.add_argument(
        "--manifest",
        default=str(REPO_ROOT / ".claude-plugin" / "marketplace.json"),
        help="Path to marketplace.json (default: REPO_ROOT/.claude-plugin/marketplace.json)",
    )
    args = parser.parse_args()

    schema_path = REPO_ROOT / ".claude-plugin" / "marketplace.schema.json"
    if not schema_path.exists():
        print(f"ERROR: schema file not found: {schema_path}")
        sys.exit(1)

    schema = json.loads(schema_path.read_text(encoding="utf-8"))

    manifest_path = Path(args.manifest)
    try:
        manifest_text = manifest_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"ERROR: manifest file not found: {manifest_path}")
        sys.exit(1)

    try:
        manifest = json.loads(manifest_text)
    except json.JSONDecodeError as e:
        print(f"ERROR: manifest JSON parse error: {e}")
        sys.exit(1)

    try:
        jsonschema.validate(manifest, schema)
    except jsonschema.ValidationError as e:
        print(f"ERROR: manifest schema validation failed: {e.message}")
        sys.exit(1)

    plugins = manifest.get("plugins", [])
    skills_validated = []
    for plugin in plugins:
        source = plugin["source"]
        # Resolve source relative to REPO_ROOT (strip leading ./ if present)
        source_path = REPO_ROOT / source.lstrip("./").lstrip("/")
        # Handle ./skills/docx style paths properly
        if source.startswith("./"):
            source_path = REPO_ROOT / source[2:]
        elif source.startswith("/"):
            source_path = Path(source)
        else:
            source_path = REPO_ROOT / source

        if not source_path.is_dir():
            print(f"ERROR: source directory not found: {source_path}")
            sys.exit(1)

        # Per-plugin layout (ADR-0002): each plugin source directory holds its
        # own skills/ subdirectory, one directory per bundled skill.
        skills_dir = source_path / "skills"
        if not skills_dir.is_dir():
            print(f"ERROR: skills directory not found in plugin source: {skills_dir}")
            sys.exit(1)

        skill_dirs = sorted(p for p in skills_dir.iterdir() if p.is_dir())
        if not skill_dirs:
            print(f"ERROR: no skill directories found in: {skills_dir}")
            sys.exit(1)

        for skill_dir in skill_dirs:
            skill_md = skill_dir / "SKILL.md"
            if not skill_md.exists():
                print(f"ERROR: SKILL.md not found in: {skill_dir}")
                sys.exit(1)

            try:
                post = frontmatter.load(str(skill_md))
            except Exception as e:
                print(f"ERROR: failed to parse frontmatter in {skill_md}: {e}")
                sys.exit(1)

            name = post.metadata.get("name", "")
            if not name:
                print(f"ERROR: 'name' field missing or empty in frontmatter: {skill_md}")
                sys.exit(1)

            description = post.metadata.get("description", "")
            if not description:
                print(f"ERROR: 'description' field missing or empty in frontmatter: {skill_md}")
                sys.exit(1)

            dir_name = skill_dir.name
            if name != dir_name:
                print(
                    f"ERROR: 'name' field in frontmatter ({name!r}) does not match "
                    f"directory name ({dir_name!r}): {skill_md}"
                )
                sys.exit(1)

            skills_validated.append(name)

    print(f"PASS: all {len(plugins)} plugins ({len(skills_validated)} skills) validated.")
    sys.exit(0)


if __name__ == "__main__":
    main()
