from mock import Mock
from nose.tools import istest, eq_

from tetris.states.main_menu import MainMenu
from tetris.visibles.menu import Menu
from tetris.visibles.factory import Factory
from tetris.engine import Engine
from tetris.states.test.test_state import TestState

#pylint: disable=attribute-defined-outside-init
class TestMainMenu(TestState):
    def create_state(self, window):
        return MainMenu(window, self.factory, self.engine)

    def setup(self):
        self.menu = Mock(Menu)
        self.engine = Mock(Engine)
        self.factory = Mock(Factory)
        self.factory.create_menu.return_value = self.menu
        TestState.setup(self)

    @istest
    def create_menu(self):
        self.when_state_init()
        self.then_create_menu_with_header("Main Menu")
        self.then_create_menu_with_row("1. Start game")
        self.then_create_menu_with_row("2. Options")
        self.then_create_menu_with_row("Esc. Exit")

    @istest
    def pressing_escape_quits_the_game(self):
        self.given_key_pressed("Esc")
        self.when_handle_event()
        self.then_quit()

    @istest
    def stay_in_state_on_other_keys(self):
        self.given_key_pressed("3")
        self.when_handle_event()
        self.then_stay_in_same_state()

    def when_state_init(self):
        self.state.init()

    def then_create_menu_with_row(self, text):
        self.menu.add_choice.assert_any_call(text)

    def then_create_menu_with_header(self, text):
        self.menu.add_header.assert_called_with(text)

    def then_quit(self):
        self.engine.stop.assert_called_with()
