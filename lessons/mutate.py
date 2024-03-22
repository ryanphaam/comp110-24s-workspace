"""Mutating functions."""

__author__ = "730710909"


def manual_append(word: list[int], number: int) -> None:
    """Appending the argument value into the list."""
    word.append(number)


def double(number: list[int]) -> None:
    """Doubling the list values."""
    counter: int = 1
    x: int = 0
    while (counter <= len(number)):
        number[x] *= 2
        x += 1
        counter += 1
