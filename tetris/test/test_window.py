#pylint: disable=W0201

from mock import Mock
from nose.tools import eq_
from tetris.wrappers.display import Display
from tetris.wrappers.surface import Surface

from tetris.window import Window

class TestWindow(object):
    def setup(self):
        self.display = Mock(Display)
        self.root = Mock(Surface)
        self.window = Window(self.display)

    def test_flip_window(self):
        self.when_draw_is_called()
        self.then_flip_buffers()

    def test_draw_children(self):
        self.given_children_amount(2)
        self.when_draw_is_called()
        self.then_draw_children(2)

    def given_children_amount(self, children):
        self.display.get_surface.return_value = self.root
        for child in range(children):
            self.window.add_child(child)

    def when_draw_is_called(self):
        self.window.draw()

    def then_flip_buffers(self):
        self.display.flip.assert_called_once_with()

    def then_draw_children(self, children):
        eq_(self.root.blit.call_count, children)
