"""Creating a Point class."""

from __future__ import annotations


class Point:
    """Point class to create coordinates for x and y."""

    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Create a new Point object."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """If function is used, point multiplied by factor."""
        self.x = self.x * factor
        self.y = self.y * factor

    def scale(self, factor: int) -> Point:
        """If function is used, new point returned."""
        new_point: Point = Point(self.x, self.y)
        new_point.x = new_point.x * factor
        new_point.y = new_point.y * factor
        return new_point