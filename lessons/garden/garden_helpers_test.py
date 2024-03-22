"""Test my garden functions."""

__author__ = "730710909"

from lessons.garden.garden_helpers import add_by_kind
from lessons.garden.garden_helpers import add_by_date
from lessons.garden.garden_helpers import lookup_by_kind_and_date


def test_add_by_kind_use() -> None:
    """Use case for when you are just adding plant to an already made key."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(by_kind, "flower", "daisy")
    assert by_kind == {"flower": ["marigold", "zinnia", "daisy"], "vegetable": ["carrots"]}


def test_add_by_kind_edge() -> None:
    """Edge case for when you are adding the same plant to a new key."""
    by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    add_by_kind(by_kind, "fruit", "marigold")
    assert by_kind == {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"], "fruit": ["marigold"]}


def test_add_by_date_use() -> None:
    """Use case for when you are adding a plant to an existing month key."""
    garden_by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    add_by_date(garden_by_date, "April", "daisy")
    assert garden_by_date == {"April": ["marigold", "daisy"], "June": ["carrots"]}


def test_add_by_date_edge() -> None:
    """Edge case for when you are adding a new date and a new plant."""
    garden_by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    add_by_date(garden_by_date, "July", "mangos")
    assert garden_by_date == {"April": ["marigold"], "June": ["carrots"], "July": ["mangos"]}


def test_lookup_by_kind_date_use() -> None:
    """Use case for finding a plant using an existing kind and month."""
    plants_by_kind: dict[str, list[str]] = {"flower": ["marigold", "zinnia"], "vegetable": ["carrots"]}
    plants_by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    kind: str = "flower"
    month: str = "April"
    plant: str = lookup_by_kind_and_date(plants_by_kind, plants_by_date, kind, month)
    assert plant == "flowers to plant in April: ['marigold']"


def test_lookup_by_kind_date_edge() -> None:
    """Edge case for finding a plant using existing kind and new date."""
    plants_by_kind: dict[str, list[str]] = {"flower": ["daisy", "zinnia"], "vegetable": ["carrots"]}
    plants_by_date: dict[str, list[str]] = {"April": ["marigold"], "June": ["carrots"]}
    kind: str = "flower"
    month: str = "April"
    plant: str = lookup_by_kind_and_date(plants_by_kind, plants_by_date, kind, month)
    assert plant == "No flowers to plant in April"