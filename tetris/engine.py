"""
This class runs the main loop.
"""

class Engine(object):
    def __init__(self, queue, factory):
        self._queue = queue
        self._factory = factory
        self._state = None
        self._running = True

    def start(self):
        self._state = self._factory.create_main_menu(self).init()
        self._loop()

    def _loop(self):
        while self._running:
            self._state.update()
            for event in self._queue.events():
                self._state.handle(event)
            self._state.draw()

    def stop(self):
        self._running = False
