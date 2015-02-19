from mock import Mock
from nose.tools import istest, eq_

from tetris.wrappers.surface import Surface
from tetris.wrappers.font import Font
from tetris.visibles.menu_row import MenuRow
from tetris.values.color import MenuRowColor

#pylint: disable=attribute-defined-outside-init
class TestMenuRow(object):
    def setup(self):
        self.parent = Mock(Surface)
        self.font = Mock(Font)
        self.menu_row = MenuRow(self.font)

    @istest
    def menu_row_font(self):
        self.when_menu_row_is_drawn()
        self.then_render_font(size=20, color=MenuRowColor())

    @istest
    def extra_space_under_menu_rows(self):
        self.when_getting_font_size()
        self.then_get_size(25)

    def when_menu_row_is_drawn(self):
        self.menu_row.draw(self.parent)

    def when_getting_font_size(self):
        self.size = self.menu_row.get_font_size()

    def then_render_font(self, text="", size=20, color=MenuRowColor()):
        self.font.write.assert_called_once_with(text, size, color)

    def then_get_size(self, size):
        eq_(self.size, size)
