from tetris.states.main_menu import MainMenu

class Factory(object):
    def __init__(self, window, factory):
        self._window = window
        self._factory = factory

    def create_main_menu(self, engine):
        return MainMenu(self._window, self._factory, engine)
