"""
A Single line of _text with no children.
"""

from tetris.visibles.component import Component, recreate_surface

class Text(Component):
    def __init__(self, font, text="", size=20, color=(255, 255, 255)):
        Component.__init__(self)
        self._font = font
        self._text = text
        self._size = size
        self._color = color

    @recreate_surface
    def set_text(self, text):
        self._text = text

    @recreate_surface
    def set_size(self, size):
        self._size = size

    @recreate_surface
    def set_color(self, color):
        self._color = color

    def get_font_size(self):
        return self._size

    def surface(self):
        return self._font.write(self._text, self._size, self._color)
