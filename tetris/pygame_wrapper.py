"""
Wraps pygame to enable unit testing of classes dependent
on pygame functions.

Responsibilities:
- Create a layer between Tetris and pygame.
"""
import pygame

class PygameWrapper(object):
    def __init__(self):
        pygame.init()

    def open_window(self, width, height):
        pygame.display.set_mode((width, height))
