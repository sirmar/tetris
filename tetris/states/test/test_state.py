from mock import Mock
from nose.tools import istest, eq_

from tetris.wrappers.event import Event
from tetris.states.state import State
from tetris.visibles.window import Window

#pylint: disable=attribute-defined-outside-init
class TestState(object):
    def create_state(self, window):
        return State(window)

    def setup(self):
        self.event = Mock(Event)
        self.window = Mock(Window)
        self.state = self.create_state(self.window)

    @istest
    def draw_screen(self):
        self.when_state_is_drawn()
        self.then_draw_window()

    @istest
    def events_dont_change_state_as_default(self):
        self.given_not_overridden()
        self.when_handle_event()
        self.then_stay_in_same_state()

    @istest
    def updates_dont_change_state_as_default(self):
        self.given_not_overridden()
        self.when_updating()
        self.then_stay_in_same_state()

    def given_not_overridden(self):
        pass

    def given_key_pressed(self, key):
        self.event.escape.return_value = False
        if key == "Esc":
            self.event.escape.return_value = True

    def when_state_is_drawn(self):
        self.state.draw()

    def when_updating(self):
        self.next_state = self.state.update()

    def when_handle_event(self):
        self.next_state = self.state.handle(self.event)

    def then_draw_window(self):
        self.window.draw.assert_called_with()

    def then_stay_in_same_state(self):
        eq_(self.next_state, self.state)
