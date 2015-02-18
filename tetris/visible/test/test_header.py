#pylint: disable=W0201

from mock import Mock
from nose.tools import istest, eq_
from tetris.wrapper.surface import Surface
from tetris.wrapper.font import Font

from tetris.visible.header import Header
from tetris.values.color import HeaderColor

class TestHeader(object):
    def setup(self):
        self.parent = Mock(Surface)
        self.font = Mock(Font)
        self.header = Header(self.font)

    @istest
    def header_font(self):
        self.when_header_is_drawn()
        self.then_render_font(size=30, color=HeaderColor())

    @istest
    def extra_space_under_headers(self):
        self.when_getting_font_size()
        self.then_get_size(40)

    def when_header_is_drawn(self):
        self.header.draw(self.parent)

    def when_getting_font_size(self):
        self.size = self.header.get_font_size()

    def then_render_font(self, text="", size=20, color=(255, 255, 255)):
        self.font.write.assert_called_once_with(text, size, color)

    def then_get_size(self, size):
        eq_(self.size, size)
