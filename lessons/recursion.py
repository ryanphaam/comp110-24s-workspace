"""Recursive practice."""


def f(n: int, k: int) -> int:
    """Function that does n * k."""
    if n == 0:
        return 0
    else:
        return f(n - 1, k) + k
