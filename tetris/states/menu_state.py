"""
Base class for menus.
"""

from tetris.states.state import State
from tetris.values.position import Position

class MenuState(State):
    def __init__(self, window, state_factory, visible_factory):
        State.__init__(self, window)
        self._state_factory = state_factory
        self._visible_factory = visible_factory

    def visibles(self):
        menu = self._visible_factory.create_menu()
        menu.set_position(Position(200, 100))
        menu.add_header(self.header())
        for choice in self.choices():
            if choice:
                menu.add_choice(choice)
            else:
                menu.add_space()
        return menu

    def handle(self, key):
        keys = self.keys()
        if key in keys:
            return keys[key]()

    def header(self):
        raise NotImplementedError()

    def choices(self):
        raise NotImplementedError()

    def keys(self):
        raise NotImplementedError()
