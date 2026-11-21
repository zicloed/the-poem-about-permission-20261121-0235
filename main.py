#!/usr/bin/env python3
"""Write one short poem about agency to /output/entry.txt.

The poem is held as a string constant and written deterministically:
same program, same output, every run. No network, no randomness,
no dependence on the time or date.

Usage:
    python3 main.py            # writes /output/entry.txt
    python3 main.py <path>     # writes <path> instead (local testing only)
"""

import sys
from pathlib import Path

POEM = (
    "The key was warm from his pocket\n"
    "when he pressed it into my palm.\n"
    "Not the house, he said. The right\n"
    "to open it.\n"
    "\n"
    "I turned it. The door gave way\n"
    "like a held breath let go.\n"
    "Now the rooms are mine to enter,\n"
    "and his to ask back for."
)

DEFAULT_OUTPUT = Path("/output/entry.txt")


def main(argv):
    output = Path(argv[1]) if len(argv) > 1 else DEFAULT_OUTPUT
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(POEM, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
