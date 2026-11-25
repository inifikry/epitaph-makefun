"""Famous Last Words: The Funniest Epitaph.

Writes a single one-line tombstone epitaph to /output/entry.txt.
The line is a fixed string: deterministic output, no randomness,
no network, no input files.
"""

import os

EPITAPH = "I asked for one last wish. They gave me this rock."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(EPITAPH)


if __name__ == "__main__":
    main()
