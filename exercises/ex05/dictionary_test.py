"""Dictionary testing file."""

__author__ = "730710909"

import pytest
from exercises.ex05.dictionary import invert
from exercises.ex05.dictionary import favorite_color
from exercises.ex05.dictionary import count
from exercises.ex05.dictionary import alphabetizer
from exercises.ex05.dictionary import update_attendance


def test_invert_use1() -> None:
    """Use case for when you are trying to invert different letters."""
    input: dict[str, str] = {'a': 'z', 'b': 'y', 'c': 'x'}
    inverted_dict: dict[str, str] = {}
    inverted_dict: dict = invert(input)
    assert inverted_dict == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_use2() -> None:
    """Use case for when you are inverting words."""
    input: dict[str, str] = {'apple': 'cat', 'dog': 'banana'}
    inverted_dict: dict[str, str] = {}
    inverted_dict = invert(input)
    assert inverted_dict == {'cat': 'apple', 'banana': 'dog'}


def test_invert_edge() -> None:
    """Edge case for when the values are the same."""
    with pytest.raises(KeyError):
        my_dictionary = {'alyssa': 'byrnes', 'adam': 'byrnes'}
        invert(my_dictionary)


def test_favorite_color_use1() -> None:
    """Use case to test when one color appears the most."""
    input: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    max_color: str = favorite_color(input)
    assert max_color == "blue"


def test_favorite_color_use2() -> None:
    """Use case to test with more colors and more numbers."""
    input: dict[str, str] = {"Marc": "yellow", "Ezri": "brown", "Kris": "brown", "Josh": "green", "Alan": "purple", "Yash": "red"}
    max_color: str = favorite_color(input)
    assert max_color == "brown"


def test_favorite_color_edge() -> None:
    """Edge case to test if the colors are tied that the first color that appears is returned."""
    input: dict[str, str] = {"Marc": "yellow", "Ryan": "yellow", "Ezri": "blue", "Kris": "blue"}
    max_color: str = favorite_color(input)
    assert max_color == "yellow"


def test_count_use1() -> None:
    """Use case to count when a value appears multiple times."""
    input: list[str] = ["love", "key", "Justin", "key", "love", "love"]
    dictionary: dict[str, int] = count(input)
    assert dictionary == {"love": 3, "key": 2, "Justin": 1}


def test_count_use2() -> None:
    """Use case to count values that do not repeat."""
    input: list[str] = ["Josh", "life", "YouTube", "Vaseline", "chair", "table", "laptop"]
    dictionary: dict[str, int] = count(input)
    assert dictionary == {"Josh": 1, "life": 1, "YouTube": 1, "Vaseline": 1, "chair": 1, "table": 1, "laptop": 1}


def test_count_edge() -> None:
    """Edge case when there is only one value."""
    input: list[str] = ["love"]
    dictionary: dict[str, int] = count(input)
    assert dictionary == {"love": 1}


def test_alphabetizer_use1() -> None:
    """Use case to organize a list of words."""
    input: list[str] = ["cat", "apple", "boy", "angry", "bad", "car"]
    dictionary: dict[str, list[str]] = alphabetizer(input)
    assert dictionary == {'c': ['cat', 'car'], 'a': ['apple', 'angry'], 'b': ['boy', 'bad']}


def test_alphabetizer_use2() -> None:
    """Use case to organize but with a capitalized letter in a word."""
    input: list[str] = ["Python", "sugar", "Turtle", "party", "table"]
    dictionary: dict[str, list[str]] = alphabetizer(input)
    assert dictionary == {'p': ['Python', 'party'], 's': ['sugar'], 't': ['Turtle', 'table']}


def test_alphabetizer_edge() -> None:
    """Edge case to organize two of the same words."""
    input: list[str] = ["cat", "cat"]
    dictionary: dict[str, list[str]] = alphabetizer(input)
    assert dictionary == {'c': ['cat', 'cat']}


def test_update_attendance_use1() -> None:
    """Use case to update a weekday that already exists."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(attendance_log, "Tuesday", "Vrinda")
    assert attendance_log == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa", "Vrinda"]}


def test_update_attendance_use2() -> None:
    """Use case to update a weekday that doesn't exist."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(attendance_log, "Wednesday", "Vrinda")
    assert attendance_log == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"], "Wednesday": ["Vrinda"]}


def test_update_attendance_edge() -> None:
    """Edge case to update a weekday and name that already exists in that day."""
    attendance_log: dict[str, list[str]] = {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}
    update_attendance(attendance_log, "Tuesday", "Alyssa")
    assert attendance_log == {"Monday": ["Vrinda", "Kaleb"], "Tuesday": ["Alyssa"]}