"""

"""

#pylint: disable=invalid-name
class Size(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._check_ranges()

    def __eq__(self, o):
        same_type = isinstance(o, Size)
        return same_type and self.width == o.width and self.height == o.height

    def __repr__(self):
        return "Size(%s, %s)" % (self.width, self.height)

    def tuple(self):
        return (self.width, self.height)

    def _check_ranges(self):
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Invalid size: %s" % self)

class BlockSize(Size):
    def __init__(self):
        Size.__init__(self, 10, 10)
