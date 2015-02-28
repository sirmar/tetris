from mock import Mock
from nose.tools import istest

from tetris.wrappers.event_queue import EventQueue
from tetris.wrappers.event import Event
from tetris.states.factory import Factory
from tetris.engine import Engine
from tetris.states.main_menu import MainMenu

#pylint: disable=attribute-defined-outside-init
class TestEngine(object):
    def setup(self):
        self.queue = Mock(EventQueue)
        self.event = Mock(Event)
        self.main_menu = Mock(MainMenu)
        self.factory = Mock(Factory)
        self.factory.create_main_menu.return_value = self.main_menu
        self.engine = Engine(self.queue, self.factory)

    # @istest
    # def read_from_event_queue(self):
    #     self.given_waiting_events()
    #     self.when_engine_has_started()
    #     self.then_read_events_from_queue()


    # @istest
    # def add_menu_to_scene(self):
    #     self.when_engine_has_started()
    #     self.then_show_main_menu()

    def given_engine_started(self):
        self.when_engine_has_started()

    def given_waiting_events(self):
        self.queue.events.return_value = [self.event]

    def when_engine_has_started(self):
        self.when_escape_pressed()
        self.engine.start()

    def then_read_events_from_queue(self):
        self.event.escape.assert_called_once_with()

    def then_draw_screen(self):
        self.window.draw.assert_called_once_with()

    def then_show_main_menu(self):
        self.factory.create_main_menu.assert_called_once_with()
