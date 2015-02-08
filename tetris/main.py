"""
This is the main class of this Tetris game.

Responsibilities:
- Instantiate all objects.
- Start the game.
"""

from tetris.window import Window
from tetris.pygame_wrapper import PygameWrapper

class Tetris(object):
    def __init__(self):
        pygame = PygameWrapper()
        self.window = Window(pygame)

    def run(self):
        """Runs the program"""
        self.window.open(640, 480)

if __name__ == '__main__':
    Tetris().run()
