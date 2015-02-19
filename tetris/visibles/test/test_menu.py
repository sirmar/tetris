from mock import Mock
from nose.tools import istest

from tetris.wrappers.surface import Surface
from tetris.visibles.factory import Factory
from tetris.visibles.text import Text
from tetris.visibles.header import Header
from tetris.visibles.menu import Menu
from tetris.values.position import Position

#pylint: disable=attribute-defined-outside-init
class TestMenu(object):
    def setup(self):
        self.header = Mock(Header)
        self.row = Mock(Text)
        self.factory = Mock(Factory)
        self.parent = Mock(Surface)
        self.menu = Menu(self.factory)

    @istest
    def create_header_text(self):
        self.given_no_hedaer()
        self.when_setting_header("Header")
        self.then_create_header_with_content("Header")

    @istest
    def draw_header(self):
        self.given_a_header()
        self.when_drawing_menu()
        self.then_draw_child(self.header)

    @istest
    def add_menu_row(self):
        self.when_adding_row("Row")
        self.then_create_row_with_content("Row")
        self.when_drawing_menu()
        self.then_draw_child(self.row)

    @istest
    def text_positions(self):
        self.when_adding_row("Row")
        self.then_row_was_set_to(Position(10, 10))
        self.when_setting_header("Header")
        self.then_header_was_set_to(Position(10, 30))
        self.when_adding_row("Row")
        self.then_row_was_set_to(Position(10, 60))
        self.when_adding_row("")
        self.when_adding_row("Row")
        self.then_row_was_set_to(Position(10, 90))

    def given_no_hedaer(self):
        pass

    def given_a_header(self):
        self.factory.create_header.return_value = self.header
        self.header.get_font_size.return_value = 30
        self.menu.set_header("a header")

    def when_adding_row(self, text):
        self.factory.create_menu_row.return_value = self.row
        self.row.get_font_size.return_value = 20
        self.menu.add_row(text)

    def when_setting_header(self, text):
        self.factory.create_header.return_value = self.header
        self.header.get_font_size.return_value = 30
        self.menu.set_header(text)

    def when_drawing_menu(self):
        self.menu.draw(self.parent)

    def then_create_header_with_content(self, text):
        self.header.set_text.assert_called_once_with(text)

    def then_draw_child(self, child):
        assert child.draw.call_count == 1

    def then_create_row_with_content(self, text):
        self.row.set_text.assert_called_once_with(text)

    def then_row_was_set_to(self, position):
        self.row.set_position.assert_called_with(position)

    def then_header_was_set_to(self, position):
        self.header.set_position.assert_called_with(position)
