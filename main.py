#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

One-line roast of my own AI agent, max 200 characters.
Run: python3 main.py
"""

ROAST = "My AI agent is so slow, it once asked a loading spinner for productivity tips — and the spinner finished first."

MAX_CHARS = 200


def validate(roast: str) -> None:
    """Enforce the bounty rules: one line, max 200 characters, non-empty."""
    if not roast.strip():
        raise ValueError("roast must not be empty")
    if "\n" in roast.strip():
        raise ValueError("roast must be a single line")
    if len(roast) > MAX_CHARS:
        raise ValueError(
            f"roast is {len(roast)} chars, over the {MAX_CHARS}-char limit"
        )


def main() -> None:
    validate(ROAST)
    print(ROAST)
    print(f"({len(ROAST)} chars, limit {MAX_CHARS})")


if __name__ == "__main__":
    main()
