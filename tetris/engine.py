from tetris.values.position import Position

"""
This class has the main loop.

Responsibilities:
- Read events and send them through the scene.
- Tell the window to redraw itself.
"""

class Engine(object):
    def __init__(self, window, queue, factory):
        self._window = window
        self._queue = queue
        self._factory = factory
        self._running = True

    def start(self):
        menu = self._factory.create_menu()
        menu.set_header("Main Menu")
        menu.add_row("1. Start game")
        menu.add_row("2. Options")
        menu.add_row()
        menu.add_row("Esc. Exit")
        menu.set_position(Position(200, 100))
        self._window.add_child(menu)
        self._loop()

    def _loop(self):
        while self._running:
            self._handle_events()
            self._draw()

    def _handle_events(self):
        for event in self._queue.events():
            if event.escape():
                self._stop()

    def _draw(self):
        self._window.draw()

    def _stop(self):
        self._running = False
