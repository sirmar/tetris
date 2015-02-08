from mock import Mock
from tetris.window import Window
from tetris.pygame_wrapper import PygameWrapper

class TestWindow(object):
    def setup(self):
        self.pygame = Mock(PygameWrapper)
        self.window = Window(self.pygame)

    def test_open_window(self):
        self.when_open_is_called_with_size(640, 480)
        self.then_show_a_window_sized(640, 480)

    def when_open_is_called_with_size(self, width, height):
        self.window.open(width, height)

    def then_show_a_window_sized(self, width, height):
        self.pygame.open_window.assert_called_once_with(width, height)
