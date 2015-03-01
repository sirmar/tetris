from mock import Mock
from nose.tools import istest

from tetris.wrappers.display import Display
from tetris.visibles.window import Window

#pylint: disable=attribute-defined-outside-init
class TestWindow(object):
    def setup(self):
        self.display = Mock(Display)
        self.window = Window(self.display)

    @istest
    def flip_buffer_on_draw(self):
        self.when_draw_is_called()
        self.then_flip_buffers()

    @istest
    def clear_screen_on_draw(self):
        self.when_draw_is_called()
        self.then_clear_screen()

    def when_draw_is_called(self):
        self.window.draw()

    def then_flip_buffers(self):
        self.display.flip.assert_called_once_with()

    def then_clear_screen(self):
        self.display.clear.assert_called_once_with()
