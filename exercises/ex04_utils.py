"""EX03 - Util exercise."""

__author__ = "730710909"


def all(x: list[int], y: int) -> bool:
    """Seeing if y is equal to all of x list."""
    if len(x) == 0:
        return False
    
    for elem in x:
        if (elem != y):
            return False
    return True


def max(z: list[int]) -> int:
    """Checking which number in list is the max."""
    if len(z) == 0:
        raise ValueError("max() arg is an empty List")
    max_value = z[0]
    for index in z:
        if (index > max_value):
            max_value = index
    return max_value


def is_equal(g: list[int], h: list[int]) -> bool:
    """Checking to see if both lists are equal to each other."""
    if len(g) != len(h):
        return False
    
    for i in range(len(g)):
        if g[i] != h[i]:
            return False
    return True


def extend(j: list[int], k: list[int]) -> None:
    """Appending 1st list to 2nd list."""
    for elem in k:
        j.append(elem)