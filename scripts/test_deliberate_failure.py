"""
test_deliberate_failure.py — Asserts that the validator catches bad-skill.

This script owns ALL fixture-related assertions. It runs validate_structure.py
against a synthetic manifest that includes the bad-skill fixture and asserts
that the validator exits non-zero. It also asserts that the fixture has not
been accidentally contaminated with a SKILL.md file.

Path resolution: all paths are resolved relative to the script file's own
location using pathlib:
    REPO_ROOT = Path(__file__).parent.parent.resolve()
This means the script produces consistent results regardless of the working
directory from which it is invoked.

Exit codes:
    0 — Validator correctly caught bad-skill (expected behaviour).
    1 — Validator did not catch bad-skill (auditor is broken), OR
        fixture has been contaminated.
"""

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent.resolve()


def main():
    bad_skill_dir = REPO_ROOT / "tests" / "fixtures" / "bad-skill"
    contamination_path = bad_skill_dir / "SKILL.md"

    if contamination_path.exists():
        print(
            "FAILURE: bad-skill fixture has been contaminated with SKILL.md — "
            "remove it to restore the fixture."
        )
        sys.exit(1)

    manifest_path = REPO_ROOT / ".claude-plugin" / "marketplace.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    manifest["plugins"].append(
        {
            "name": "bad-skill",
            "source": "./tests/fixtures/bad-skill",
            "description": "Deliberate-failure fixture",
        }
    )

    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
    try:
        json.dump(manifest, tmp)
        tmp.flush()
        tmp.close()
        result = subprocess.run(
            [
                sys.executable,
                str(REPO_ROOT / "scripts" / "validate_structure.py"),
                "--manifest",
                tmp.name,
            ],
            capture_output=True,
        )
    finally:
        os.unlink(tmp.name)

    if result.returncode == 0:
        print("FAILURE: validator did not catch bad-skill — auditor is broken.")
        sys.exit(1)

    print("PASS: validator correctly caught bad-skill.")
    sys.exit(0)


if __name__ == "__main__":
    main()
