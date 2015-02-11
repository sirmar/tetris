from pygame import display
from tetris.wrappers.surface import Surface

class Display(object):
    def __init__(self):
        self.screen = display.set_mode((640, 480))

    def flip(self):
        display.flip()

    def clear(self):
        self.screen.fill((0, 0, 0))

    def get_surface(self):
        return Surface(self.screen)
