from pygame import font
from tetris.wrapper.surface import Surface

class Font(object):
    def __init__(self):
        font.init()
        self._menu = font.SysFont("arial", 24)

    def write(self, text):
        surface = self._menu.render(text, True, (0, 128, 0))
        return Surface(surface)
