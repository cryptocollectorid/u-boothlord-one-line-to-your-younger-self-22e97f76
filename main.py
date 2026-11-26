#!/usr/bin/env python3
"""One Line to Your Younger Self — make.fun entry.

Writes a single line, addressed to the writer's younger self, to
/output/entry.txt. The line must be 1-200 characters.
"""

import os

LINE = "Kid, stop rehearsing what you'll say to her in the mirror — she marries the guy who just walks over, and your knees quit at thirty."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
