from pygame import font
from tetris.wrapper.surface import Surface

class Font(object):
    def __init__(self):
        font.init()

    def write(self, text, size, color):
        sysfont = font.SysFont("arial", size)
        surface = sysfont.render(text, False, color)
        return Surface(surface)
