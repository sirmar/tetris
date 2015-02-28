"""
This is the main class of this Tetris game.
"""

from tetris.factory import Factory

class Tetris(object):
    def __init__(self):
        self.factory = Factory()

    def run(self):
        self.factory.create_engine().start()

def main():
    return Tetris().run()
