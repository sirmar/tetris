#pylint: disable=W0201

from mock import Mock
from nose.tools import istest

from tetris.wrapper.surface import Surface
from tetris.visible.factory import Factory
from tetris.visible.text import Text
from tetris.visible.header import Header
from tetris.visible.menu import Menu

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
    def change_header_text(self):
        self.given_a_header()
        self.when_setting_header("Header")
        self.then_reuse_header()

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
        self.given_a_header()
        self.when_adding_row("Row")
        self.then_row_position_is((0, 30))
        self.when_adding_row("Row")
        self.then_row_position_is((0, 50))
        self.when_adding_row("")
        self.when_adding_row("Row")
        self.then_row_position_is((0, 80))

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

    def then_reuse_header(self):
        assert self.factory.create_header.call_count == 1
        assert self.header.set_text.call_count == 2

    def then_draw_child(self, child):
        assert child.draw.call_count == 1

    def then_create_row_with_content(self, text):
        self.row.set_text.assert_called_once_with(text)

    def then_row_position_is(self, position):
        self.row.set_position.assert_called_with(position)
