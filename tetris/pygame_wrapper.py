"""
Wraps pygame to enable unit testing of classes dependent
on pygame functions.

Responsibilities:
- Create a layer between Tetris and pygame.
"""

import pygame

KEYS = {
    pygame.K_ESCAPE : "Escape"
}

class PygameWrapper(object):
    def __init__(self):
        pygame.init()
        self._font = pygame.font.SysFont("arial", 24)
        self._screen = None

    def open_window(self, width, height):
        self._screen = pygame.display.set_mode((width, height))

    def write(self, text):
        font = self._font.render(text, True, (0, 128, 0))
        self._screen.blit(font, (0, 0))

    def get_keys(self):
        events = []
        for event in pygame.event.get():
            if event.type == pygame.KEYUP and KEYS.has_key(event.key):
                events.append(KEYS[event.key])
        return events

    def quit(self):
        pygame.quit()

    def flip_screen(self):
        pygame.display.flip()
