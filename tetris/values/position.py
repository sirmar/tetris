#pylint: disable=C0103

class Position(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        same_type = isinstance(other, Position)
        return same_type and self.x == other.x and self.y == other.y
