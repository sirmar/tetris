from mock import Mock
from nose.tools import istest, eq_
from tetris.wrappers.surface import Surface
from tetris.wrappers.font import Font

from tetris.visibles.text import Text

#pylint: disable=attribute-defined-outside-init
class TestText(object):
    def setup(self):
        self.parent = Mock(Surface)
        self.surface = Mock(Surface)
        self.font = Mock(Font)
        self.text = Text(self.font)

    @istest
    def blit_text(self):
        self.given().a_text("Some text").at_position((10, 30))
        self.when_text_is_drawn()
        self.then_blit_at_position((10, 30))

    @istest
    def create_surface_once_for_same_text(self):
        self.given().a_text("Some text")
        self.when_text_is_drawn()
        self.when_text_is_drawn()
        self.then_render_font_times(1)

    @istest
    def default_font_size_is_20(self):
        self.when_text_is_drawn()
        self.then_render_font(size=20)

    @istest
    def default_color_is_white(self):
        self.when_text_is_drawn()
        self.then_render_font(color=(255, 255, 255))

    @istest
    def change_font_size(self):
        self.given().of_size(10)
        self.when_text_is_drawn()
        self.then_render_font(size=10)

    @istest
    def change_color(self):
        self.given().of_color((1, 2, 3))
        self.when_text_is_drawn()
        self.then_render_font(color=(1, 2, 3))

    @istest
    def text_size_and_color_make_dirty(self):
        self.given().a_text("Foo").of_size(10).of_color((0, 0, 0))
        self.when_text_is_drawn()
        self.given().a_text("Bar")
        self.when_text_is_drawn()
        self.given().of_size(12)
        self.when_text_is_drawn()
        self.given().of_color((10, 0, 0))
        self.when_text_is_drawn()
        self.then_render_font_times(4)

    @istest
    def get_font_size(self):
        self.given().of_size(10)
        self.when_getting_font_size()
        self.then_size_is(10)

    def given(self):
        return self

    def a_text(self, text):
        self.text.set_text(text)
        return self

    def at_position(self, position):
        self.text.set_position(position)
        return self

    def of_size(self, size):
        self.text.set_size(size)
        return self

    def of_color(self, color):
        self.text.set_color(color)
        return self

    def when_text_is_drawn(self):
        self.font.write.return_value = self.surface
        self.text.draw(self.parent)

    def when_getting_font_size(self):
        self.size = self.text.get_font_size()

    def then_blit_at_position(self, position):
        self.parent.blit.assert_called_once_with(self.surface, position)

    def then_render_font_times(self, times):
        eq_(self.font.write.call_count, times)

    def then_render_font(self, text="", size=20, color=(255, 255, 255)):
        self.font.write.assert_called_once_with(text, size, color)

    def then_size_is(self, size):
        eq_(self.size, size)
