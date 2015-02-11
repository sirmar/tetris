"""
This class has the main loop.

Responsibilities:
- Read events and send them through the scene.
- Tell the window to redraw itself.
"""
class Engine(object):
    def __init__(self, window, queue, font):
        self._window = window
        self._queue = queue
        self._font = font
        self._running = True

    def start(self):
        self._loop()

    def _loop(self):
        menu = self._font.write("Esc: Exit")
        self._window.add_child(menu)
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
