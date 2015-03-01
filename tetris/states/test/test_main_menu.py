from mock import Mock, patch
from nose.tools import istest

from tetris.states.main_menu import MainMenu
from tetris.visibles.menu import Menu
from tetris.visibles.factory import Factory as VisibleFactory
from tetris.states.factory import Factory as StateFactory
from tetris.states.options_menu import OptionsMenu

from tetris.states.test.test_state_base import TestStateBase
from tetris.wrappers.event import Event

#pylint: disable=attribute-defined-outside-init
class TestMainMenu(TestStateBase):
    def setup(self):
        self.options_menu = Mock(OptionsMenu)
        self.state_factory = Mock(StateFactory)
        self.state_factory.create_options_menu.return_value = self.options_menu

        self.menu = Mock(Menu)
        self.visible_factory = Mock(VisibleFactory)
        self.visible_factory.create_menu.return_value = self.menu

        self.start_state(
            MainMenu(self._window, self.state_factory, self.visible_factory))

    @istest
    def create_menu(self):
        self.when_state_init()
        self.then_create_menu_with_header("Main Menu")
        self.then_create_menu_with_row("1. Start game")
        self.then_create_menu_with_row("2. Options")
        self.then_create_menu_with_row("Esc. Exit")

    @istest
    @patch.object(Event, 'send_quit_event')
    def pressing_escape_quits_the_game(self, send_quit_event):
        self.given_key_pressed("Esc")
        self.when_handle_event()
        self.then_quit(send_quit_event)

    @istest
    def option_choice_will_go_to_option_menu(self):
        self.given_key_pressed("2")
        self.when_handle_event()
        self.then_go_to_state(self.options_menu)

    @istest
    def stay_in_state_on_other_keys(self):
        self.given_key_pressed("3")
        self.when_handle_event()
        self.then_stay_in_same_state()

    def then_create_menu_with_row(self, text):
        self.menu.add_choice.assert_any_call(text)

    def then_create_menu_with_header(self, text):
        self.menu.add_header.assert_called_with(text)

    def then_quit(self, send_quit_event):
        send_quit_event.assert_called_with()
