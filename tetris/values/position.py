"""
Represents a two dimensional position in space. Treat it as
an immutable. All methods should return a new Position.

Responsibilities:
- Hold x and y positions.
- Provide an interface for transforming positions.
"""

#pylint: disable=invalid-name
class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, o):
        same_type = isinstance(o, Position)
        return same_type and self.x == o.x and self.y == o.y

    def __add__(self, o):
        return self.move(o.x, o.y)

    def __repr__(self):
        return "Position(%s, %s)" % (self.x, self.y)

    def move(self, dx, dy):
        return Position(self.x + dx, self.y + dy)

    def right(self, dx=1):
        return self.move(dx, 0)

    def left(self, dx=1):
        return self.move(-dx, 0)

    def down(self, dy=1):
        return self.move(0, dy)

    def up(self, dy=1):
        return self.move(0, -dy)

    def tuple(self):
        return (self.x, self.y)
