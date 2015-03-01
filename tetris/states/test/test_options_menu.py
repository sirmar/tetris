from mock import Mock
from nose.tools import istest

from tetris.states.options_menu import OptionsMenu
from tetris.states.main_menu import MainMenu
from tetris.visibles.factory import Factory as VisibleFactory
from tetris.states.factory import Factory as StateFactory
from tetris.visibles.menu import Menu
from tetris.states.test.test_state_base import TestStateBase
from tetris.values.key import Key

#pylint: disable=attribute-defined-outside-init
class TestOptionsMenu(TestStateBase):
    def setup(self):
        self.menu = Mock(Menu)

        self.main_menu = Mock(MainMenu)
        self.state_factory = Mock(StateFactory)
        self.state_factory.create_main_menu.return_value = self.main_menu

        self.menu = Mock(Menu)
        self.visible_factory = Mock(VisibleFactory)
        self.visible_factory.create_menu.return_value = self.menu

        self.start_state(OptionsMenu(
            self._window, self.state_factory, self.visible_factory))

    @istest
    def create_menu(self):
        self.when_state_init()
        self.then_create_menu_with_header("Options")
        self.then_create_menu_with_row("1. Change name")
        self.then_create_menu_with_row("Esc. Main Menu")

    @istest
    def stay_in_state_on_other_keys(self):
        self.given_key_pressed(Key("2"))
        self.when_handle_event()
        self.then_stay_in_same_state()

    @istest
    def back_to_main_menu(self):
        self.given_key_pressed(Key("Esc"))
        self.when_handle_event()
        self.then_go_to_state(self.main_menu)

    def then_create_menu_with_row(self, text):
        self.menu.add_choice.assert_any_call(text)

    def then_create_menu_with_header(self, text):
        self.menu.add_header.assert_called_with(text)
