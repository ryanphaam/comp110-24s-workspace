"""Summing the elements of a list using different loops."""

__author__ = "730710909"


def w_sum(vals: list[float]) -> float:
    """Using while loop for summation."""
    x: int = 0
    sum: float = 0.0
    while (x < len(vals)):
        sum += vals[x]
        x += 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Using for loop for summation."""
    sum: float = 0.0
    for elem in vals:
        sum += elem
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Using for in range for summation."""
    sum: float = 0.0
    for index in range(0, len(vals)):
        sum += vals[index]
    return sum