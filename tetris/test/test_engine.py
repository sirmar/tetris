from mock import Mock
from nose.tools import istest

from tetris.wrapper.event_queue import EventQueue
from tetris.wrapper.event import Event
from tetris.visible.factory import Factory
from tetris.engine import Engine
from tetris.visible.window import Window

#pylint: disable=attribute-defined-outside-init
class TestEngine(object):
    def setup(self):
        self.window = Mock(Window)
        self.queue = Mock(EventQueue)
        self.event = Mock(Event)
        self.factory = Mock(Factory)
        self.engine = Engine(self.window, self.queue, self.factory)

    @istest
    def read_from_event_queue(self):
        self.given_waiting_events()
        self.when_engine_has_started()
        self.then_read_events_from_queue()

    @istest
    def quit_after_pressing_escape(self):
        self.given_engine_started()
        self.when_escape_pressed()
        self.then_quit()

    @istest
    def draw_screen(self):
        self.when_engine_has_started()
        self.then_draw_screen()

    @istest
    def add_menu_to_scene(self):
        self.when_engine_has_started()
        self.then_add_menu_to_scene()

    def given_engine_started(self):
        self.when_engine_has_started()

    def given_waiting_events(self):
        self.queue.events.return_value = [self.event]

    def when_engine_has_started(self):
        self.when_escape_pressed()
        self.engine.start()

    def when_escape_pressed(self):
        self.event.escape.return_value = True
        self.queue.events.return_value = [self.event]

    def then_read_events_from_queue(self):
        self.event.escape.assert_called_once_with()

    def then_quit(self):
        #TODO: access non public.
        assert not self.engine._running

    def then_draw_screen(self):
        self.window.draw.assert_called_once_with()

    def then_add_menu_to_scene(self):
        assert self.window.add_child.called
