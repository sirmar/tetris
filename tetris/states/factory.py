from tetris.states.main_menu import MainMenu
from tetris.states.options_menu import OptionsMenu

class Factory(object):
    def __init__(self, window, visible_factory):
        self._window = window
        self._visible_factory = visible_factory

    def create_main_menu(self):
        return MainMenu(self._window, self, self._visible_factory)

    def create_options_menu(self):
        return OptionsMenu(self._window, self, self._visible_factory)
