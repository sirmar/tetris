"""
Represents the game main menu screen.
"""

from tetris.values.position import Position
from tetris.states.state import State

class MainMenu(State):
    def __init__(self, window, factory, engine):
        State.__init__(self, window)
        self._factory = factory
        self._engine = engine

    def visibles(self):
        menu = self._factory.create_menu()
        menu.add_header("Main Menu")
        menu.add_choice("1. Start game")
        menu.add_choice("2. Options")
        menu.add_space()
        menu.add_choice("Esc. Exit")
        menu.set_position(Position(200, 100))
        return menu

    def handle(self, event):
        if event.escape():
            self._engine.stop()
        return self
