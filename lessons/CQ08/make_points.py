"""Testing file."""

from lessons.CQ08.point import Point


point: Point = Point(3.5, 2.0)
point.scale_by(2)
print(point.x)
print(point.y)

new_point: Point = Point(3.5, 2.0)
new_point_return = new_point.scale(2)
print(new_point.x)
print(new_point.y)