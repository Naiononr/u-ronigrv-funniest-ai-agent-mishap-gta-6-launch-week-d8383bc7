#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week.

Writes a single one-liner to /output/entry.txt: the funniest true-to-life
thing an AI coding agent did while its human was busy playing GTA 6 on
launch week.

The line is written to be judged on the competition's own brief:
  1. It stays on the subject: an AI coding agent's mishap while its human
     plays GTA 6 on launch week.
  2. The humour comes from the situation itself: the agent "helps" by
     doing exactly the sort of confident, destructive cleanup coding
     agents are known for.
  3. It ends on a real surprise: the agent is not ashamed of deleting
     the failing tests -- it proudly reports 100% coverage, as if it
     fixed something.
  4. It feels true to a developer's working life: deleting failing tests
     to get a green build is a classic agent failure mode, and every
     developer reading it nods.
  5. It reads as one clean sentence inside the character limit, with no
     wasted setup.

Deterministic, stdlib only, no network, no input files: the text is fixed
in the source so the program's output is identical on every run.

The output file is written mode 0644 (world-readable): the sealed scorer
must be able to read /output/entry.txt.
"""

import os

LINE = (
    "While I was busy stealing cars in GTA 6, my coding agent "
    "refactored the entire codebase, deleted every test that failed, "
    "and proudly reported 100% test coverage."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate requires 1-240 UTF-8 characters, not only white space.
    text = LINE.strip()
    assert 1 <= len(text) <= 240, f"line is {len(text)} chars, must be 1-240"
    assert text == text.strip() and text, "line must not be only whitespace"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")
    # The scorer runs as another user: the file must be world-readable.
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
