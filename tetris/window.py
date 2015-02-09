"""
This class do things related to the main window.

Responsibilities:
- Open the game window.
"""
class Window(object):
    def __init__(self, pygame):
        self._pygame = pygame

    def open(self, width, height):
        self._pygame.open_window(width, height)

    def flip(self):
        self._pygame.flip_screen()
