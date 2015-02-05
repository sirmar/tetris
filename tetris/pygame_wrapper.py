import pygame

class PygameWrapper(object):
    def __init__(self):
        pygame.init()

    def open_window(self, width, height):
        pygame.display.set_mode((width, height))
