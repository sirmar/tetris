from tetris.visibles.window import Window
from tetris.visibles.factory import Factory as VisibleFactory

from tetris.states.factory import Factory as StateFactory

from tetris.wrappers.event import Event
from tetris.wrappers.display import Display
from tetris.wrappers.font import Font
from tetris.engine import Engine

class Factory(object):
    def create_engine(self):
        event = Event()
        state_factory = self._state_factory()
        return Engine(event, state_factory)

    def _visible_factory(self):
        return VisibleFactory(Font())

    def _state_factory(self):
        window = Window(Display())
        visible_factory = self._visible_factory()
        return StateFactory(window, visible_factory)
