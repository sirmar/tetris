from mock import Mock
from nose.tools import eq_

from tetris.wrappers.event import Event
from tetris.visibles.window import Window

#pylint: disable=attribute-defined-outside-init
class TestStateBase(object):
    def __init__(self):
        self._event = Mock(Event)
        self._window = Mock(Window)

    def start_state(self, state):
        self._state = state

    def side(self, arg):
        return (arg == self.key)

    def given_key_pressed(self, key):
        self.return_value = False
        self._event.number.side_effect = None
        self._event.escape.return_value = False
        if key == "Esc":
            self._event.escape.return_value = True
        else:
            self.key = key
            self._event.number.side_effect = self.side

    def when_state_init(self):
        self._state.init()

    def when_updating(self):
        self._next_state = self._state.update()

    def when_handle_event(self):
        self._next_state = self._state.handle(self._event)

    def then_remove_all_visibles(self):
        self._window.remove_children.assert_called_once_with()

    def then_stay_in_same_state(self):
        eq_(self._next_state, self._state)

    def then_go_to_state(self, state):
        eq_(self._next_state, state)

    def when_state_is_drawn(self):
        self._state.draw()

    def then_draw_window(self):
        self._window.draw.assert_called_with()
