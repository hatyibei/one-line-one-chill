"""Entry for make.fun's "One Line, One Chill" bounty.

Writes the single scariest sentence I can to /output/entry.txt.
"""

import os

TEXT = (
    "The rescue team found the missing hiker's phone still recording at the trailhead. "
    "Its last photo showed the rescue team, taken from the treeline, one hour before they arrived."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
