"""
This class do things related to the main window.

Responsibilities:
- Open the game window.
"""
class Window(object):
    def __init__(self, pygame):
        self.pygame = pygame

    def open(self, width, height):
        self.pygame.open_window(width, height)
