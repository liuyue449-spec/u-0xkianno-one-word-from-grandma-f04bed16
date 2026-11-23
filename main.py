"""One Word From Grandma — entrypoint.

Writes the single word Grandma would text about AI to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (``/output/entry.txt`` in the grader).

The word is "computor": the way a grandma actually types "computer" —
warm, a little baffled, and unmistakably her own spelling. No network,
no randomness, no clock: the same word every run.
"""

import os
import sys

WORD = "computor"


def main() -> int:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)
    # Read it back: a word that never landed is worse than a loud failure.
    with open(target, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != WORD:
        print(f"entry.txt holds {written!r}, expected {WORD!r}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
