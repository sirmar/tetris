#pylint: disable=W0201

from mock import Mock
from tetris.engine import Engine
from tetris.window import Window
from tetris.pygame_wrapper import PygameWrapper

class TestEngine(object):
    def setup(self):
        self.pygame = Mock(PygameWrapper)
        self.window = Window(self.pygame)
        self.engine = Engine(self.pygame, self.window)

    def test_write_exit_option_in_start_menu(self):
        self.when_engine_is_started()
        self.then_menu_item_exists("Esc: Exit")

    def test_quit_after_pressing_escape(self):
        self.given_window_opened()
        self.when_key_pressed("Escape")
        self.then_quit()

    def test_should_flip_screen_buffer(self):
        self.when_engine_is_started()
        self.then_flip_screen()

    def given_window_opened(self):
        self.when_engine_is_started()

    def when_engine_is_started(self):
        self.when_key_pressed("Escape")
        self.engine.start(640, 480)

    def when_key_pressed(self, key):
        self.pygame.get_keys.return_value = [key]

    def then_menu_item_exists(self, menu_item):
        self.pygame.write.assert_called_once_with(menu_item)

    def then_quit(self):
        self.pygame.quit.assert_called_once_with()

    def then_flip_screen(self):
        self.pygame.flip_screen.assert_called_once_with()
