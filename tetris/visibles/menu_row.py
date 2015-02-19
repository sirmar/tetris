from tetris.visibles.text import Text
from tetris.values.color import MenuRowColor

class MenuRow(Text):
    def __init__(self, font):
        Text.__init__(self, font, size=20, color=MenuRowColor())
        self._space = 5

    def get_font_size(self):
        return Text.get_font_size(self) + self._space
