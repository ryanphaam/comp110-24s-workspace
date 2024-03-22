"""Dictionary file function."""

__author__ = "730710909"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Invert the dictionary."""
    inverted_dict: dict[str, str] = {}
    for key in input:
        new_key: str = input[key]
        if new_key not in inverted_dict:
            inverted_dict[new_key] = key
        else:
            raise KeyError(f"Key of {new_key} already exists!")
    return inverted_dict


def favorite_color(input: dict[str, str]) -> str:
    """Returns favorite/most color."""
    color_dict: dict[str, int] = {}
    max_color: str = ""
    max_count: int = 0
    for key in input:
        new_key: str = input[key]
        if new_key not in color_dict:
            color_dict[new_key] = 1
        else:
            color_dict[new_key] += 1
    for key in color_dict:
        if color_dict[key] > max_count:
            max_color = key
            max_count = color_dict[key]
    return max_color


def count(input: list[str]) -> dict[str, int]:
    """Counting the number of times that value appears in the input list."""
    dictionary: dict[str, int] = {}
    for item in input:
        if item in dictionary:
            dictionary[item] += 1
        else:
            dictionary[item] = 1
    return dictionary


def alphabetizer(input: list[str]) -> dict[str, list[str]]:
    """Alphabetize the words in the list."""
    dictionary: dict[str, list[str]] = {}
    new_list: list[str] = []
    for elem in input:
        letter: str = elem[0].lower()
        if letter not in dictionary:
            new_list.append(elem)
            dictionary[letter] = new_list
            new_list = []
        else:
            dictionary[letter].append(elem)
    return dictionary


def update_attendance(input: dict[str, list[str]], day: str, student: str) -> None:
    """This will mutate and return an updated attendance list."""
    if day not in input:
        input[day] = [student]
    elif student not in input[day]:
        input[day].append(student)