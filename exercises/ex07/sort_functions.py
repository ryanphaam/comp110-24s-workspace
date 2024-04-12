"""Functions that implement sorting algorithms."""

__author__ = "730710909"


def insertion_sort(x: list[int]) -> None:
    """Basic insertion sort algorithm. Insert into an already sorted list."""
    sorted_idx: int = 0
    list_length: int = len(x)
    while sorted_idx < list_length - 1:
        unsorted_idx: int = sorted_idx + 1
        while unsorted_idx > 0 and x[unsorted_idx] < x[unsorted_idx - 1]:
            temp: int = x[unsorted_idx]
            x[unsorted_idx] = x[unsorted_idx - 1]
            x[unsorted_idx - 1] = temp
            unsorted_idx -= 1
        sorted_idx += 1
    return None


def selection_sort(x: list[int]) -> None:
    """Basic selection sort algorithm. Repeatedly find the minimum and swap it."""
    current_idx: int = 0
    list_length: int = len(x)
    while current_idx < list_length:
        for i in range(current_idx, list_length):
            if x[i] < x[current_idx]:
                swap: int = x[i]
                x[i] = x[current_idx]
                x[current_idx] = swap
        current_idx += 1
    return None