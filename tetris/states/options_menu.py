"""
Represents the game option menu screen.
"""

from tetris.values.position import Position
from tetris.states.state import State

class OptionsMenu(State):
    def __init__(self, window, state_factory, visible_factory):
        State.__init__(self, window)
        self._state_factory = state_factory
        self._visible_factory = visible_factory

    def visibles(self):
        menu = self._visible_factory.create_menu()
        menu.add_header("Options")
        menu.add_choice("1. Change name")
        menu.add_space()
        menu.add_choice("Esc. Main Menu")
        menu.set_position(Position(200, 100))
        return menu

    def handle(self, event):
        if event.escape():
            return self._state_factory.create_main_menu()
        return self
