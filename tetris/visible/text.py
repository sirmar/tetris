"""
A Single line of _text with no children.
"""
from tetris.visible.component import Component, dirty

class Text(Component):
    def __init__(self, font, text="", size=20, color=(255, 255, 255)):
        Component.__init__(self)
        self._font = font
        self._text = text
        self._size = size
        self._color = color

    @dirty
    def set_text(self, text):
        self._text = text

    @dirty
    def set_size(self, size):
        self._size = size

    @dirty
    def set_color(self, color):
        self._color = color
        self.dirty()

    def get_font_size(self):
        return self._size

    def surface(self):
        return self._font.write(self._text, self._size, self._color)
