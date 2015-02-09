"""
This is the main class of this Tetris game.

Responsibilities:
- Instantiate all objects.
- Start the game.
"""

from tetris.window import Window
from tetris.pygame_wrapper import PygameWrapper
from tetris.engine import Engine

class Tetris(object):
    def __init__(self):
        pygame = PygameWrapper()
        window = Window(pygame)
        self.engine = Engine(pygame, window)
    def run(self):
        """Runs the program"""
        self.engine.start(640, 480)

if __name__ == '__main__':
    Tetris().run()
