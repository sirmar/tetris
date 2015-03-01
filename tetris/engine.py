"""
This class runs the main loop.
"""

from tetris.values.sys import Quit

class Engine(object):
    def __init__(self, event, factory):
        self._event = event
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
        for event in self._event.receive():
            if event == Quit():
                self.stop()
            self.set_state(self._state.handle(event))

    def set_state(self, state):
        if state and state != self._state:
            self._state = state.init()

    def stop(self):
        self._running = False
