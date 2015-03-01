"""
Represents the game option menu screen.
"""

from tetris.states.menu_state import MenuState
from tetris.values.key import Key

class OptionsMenu(MenuState):
    def __init__(self, window, state_factory, visible_factory):
        MenuState.__init__(self, window, state_factory, visible_factory)

    def header(self):
        return "Options"

    def choices(self):
        return [
            "1. Change name",
            None,
            "Esc. Main Menu",
        ]

    def keys(self):
        return {
            Key("Esc"): self._state_factory.create_main_menu,
        }
