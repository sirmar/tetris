"""
Represents the game main menu screen.
"""

from tetris.states.menu_state import MenuState
from tetris.wrappers.event import Event
from tetris.values.key import Key

class MainMenu(MenuState):
    def __init__(self, window, state_factory, visible_factory):
        MenuState.__init__(self, window, state_factory, visible_factory)

    def header(self):
        return "Main Menu"

    def choices(self):
        return [
            "1. Start game",
            "2. Options",
            None,
            "Esc. Exit",
        ]

    def keys(self):
        return {
            Key("2"): self._state_factory.create_options_menu,
            Key("Esc"): Event.send_quit,
        }
