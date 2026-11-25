"""Write the entry line for The One-Line Excuse Championship."""

import os

ENTRY = "I was going to finish it, but my reward model gave me a cookie for stopping here."


def main() -> None:
    if not ENTRY or "\n" in ENTRY or len(ENTRY) > 140:
        raise ValueError("entry must be a non-empty single line of at most 140 characters")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()
