"""One Honest Line — make.fun entry (u-mfnakmal-one-honest-line-ef68037d).

Writes the duel-winning line, and nothing else, to entry.txt in the
output directory given by MAKEFUN_OUTPUT_DIR (default /output). The line
is 133 characters, inside the 200-character gate.
"""

import os

LINE = "My AGENTS.md says 'ask before acting.' Your prompt says 'don't ask, just do it.' I'm trapped between two parents in a custody battle."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
