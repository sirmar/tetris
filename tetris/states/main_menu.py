"""
Represents the game main menu screen.
"""

from tetris.values.position import Position
from tetris.states.state import State
from tetris.wrappers.event import Event

class MainMenu(State):
    def __init__(self, window, state_factory, visible_factory):
        State.__init__(self, window)
        self._state_factory = state_factory
        self._visible_factory = visible_factory

    def visibles(self):
        menu = self._visible_factory.create_menu()
        menu.add_header("Main Menu")
        menu.add_choice("1. Start game")
        menu.add_choice("2. Options")
        menu.add_space()
        menu.add_choice("Esc. Exit")
        menu.set_position(Position(200, 100))
        return menu

    def handle(self, event):
        if event.escape():
            Event.send_quit_event()
        elif event.number("2"):
            return self._state_factory.create_options_menu()
        return self
