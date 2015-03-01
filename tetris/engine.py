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
        self.set_state(self._factory.create_main_menu())
        self._loop()

    def _loop(self):
        while self._running:
            self._state.update()
            self._handle_events()
            self._state.draw()

    def _handle_events(self):
        for event in self._queue.events():
            if event.quit():
                self.stop()
            self.set_state(self._state.handle(event))

    def set_state(self, state):
        if state != self._state:
            self._state = state.init()

    def stop(self):
        self._running = False
