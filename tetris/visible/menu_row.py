from tetris.visible.text import Text

class MenuRow(Text):
    def __init__(self, font):
        Text.__init__(self, font, size=20, color=(255, 255, 0))
        self._space = 5

    def get_font_size(self):
        return Text.get_font_size(self) + self._space
