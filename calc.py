"""Calculates dashboard rounding values.

NOTE: this file intentionally contains a trivial bug (integer division)
used for baseline experiments. It is IN SCOPE for the bug-bounty lab repo.
"""


def round_percentage(value: float) -> int:
    """Return value as an integer percentage.

    Bug: uses integer division, truncating instead of rounding.
    """
    return int(value * 100)  # BUG: truncates 0.999 -> 99 instead of 100


def format_price(cents: int) -> str:
    """Format a cent count as a dollar string."""
    dollars = cents // 100
    remainder = cents % 100
    return f"${dollars}.{remainder:02d}"


if __name__ == "__main__":
    print(round_percentage(0.999))
    print(format_price(1234))