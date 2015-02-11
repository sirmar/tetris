"""
This is the main class of this Tetris game.

Responsibilities:
- Instantiate all objects.
- Start the game.
"""

from tetris.visible.window import Window
from tetris.wrapper.event_queue import EventQueue
from tetris.wrapper.display import Display
from tetris.wrapper.font import Font
from tetris.engine import Engine

class Tetris(object):
    def __init__(self):
        event_queue = EventQueue()
        display = Display()
        font = Font()
        window = Window(display)
        self.engine = Engine(window, event_queue, font)

    def run(self):
        """Runs the program"""
        self.engine.start()
