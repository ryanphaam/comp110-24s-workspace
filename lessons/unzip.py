"""Splitting a dictionary into two lists."""

__author__ = "730710909"


def get_keys(test: dict[str, int]) -> list[str]:
    """Convertng dict to a list."""
    y: list[str] = []
    for key in test:
        y.append(key)
    return y


def get_values(test: dict[str, int]) -> list[int]:
    """Putting values into empty list."""
    y: list[int] = []
    for key in test:
        y.append(test[key])
    return y