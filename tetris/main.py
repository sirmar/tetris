"""
This is the main of this Tetris game.
"""

from tetris.window import Window
from tetris.pygame_wrapper import PygameWrapper

class Tetris(object):
    def run(self):
        """Runs the program"""
        pygame = PygameWrapper()
        Window(pygame).open(640, 480)

if __name__ == '__main__':
    Tetris().run()
