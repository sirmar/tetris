from tetris.visible.text import Text
from tetris.values.color import HeaderColor

class Header(Text):
    def __init__(self, font):
        Text.__init__(self, font, size=30, color=HeaderColor())
        self._space = 10

    def get_font_size(self):
        return Text.get_font_size(self) + self._space
