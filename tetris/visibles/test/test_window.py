from mock import Mock

from tetris.wrappers.display import Display
from tetris.visibles.window import Window

#pylint: disable=attribute-defined-outside-init
class TestWindow(object):
    def setup(self):
        self.display = Mock(Display)
        self.window = Window(self.display)

    def test_flip_window(self):
        self.when_draw_is_called()
        self.then_flip_buffers()

    def when_draw_is_called(self):
        self.window.draw()

    def then_flip_buffers(self):
        self.display.flip.assert_called_once_with()
