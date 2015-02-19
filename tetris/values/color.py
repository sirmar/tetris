"""
Represents colors. See this as an immutable. When you want another
color, just create a new one.

Responsibilities:
- Holds red, green, blue and alpha values of colors.
"""

#pylint: disable=invalid-name
class Color(object):
    def __init__(self, r=0, g=0, b=0, a=255):
        self.r = r
        self.g = g
        self.b = b
        self.a = a
        self._check_ranges()

    def __eq__(self, o):
        same_type = isinstance(o, Color)
        same_color = self.r == o.r and self.g == o.g and self.b == o.b
        same_alpha = self.a == o.a
        return same_type and same_color and same_alpha

    def __repr__(self):
        return "Color(%s, %s, %s, %s)" % (self.r, self.g, self.b, self.a)

    def tuple(self):
        return (self.r, self.g, self.b)

    def _check_ranges(self):
        if not (0 <= self.r <= 255 and
                0 <= self.g <= 255 and
                0 <= self.b <= 255 and
                0 <= self.a <= 255):
            raise ValueError("Invalid color: %s" % self)

class HeaderColor(Color):
    def __init__(self):
        Color.__init__(self, 255, 0, 0)

class MenuRowColor(Color):
    def __init__(self):
        Color.__init__(self, 255, 255, 255)

class MenuBackgroundColor(Color):
    def __init__(self):
        Color.__init__(self, 50, 50, 50, 150)
