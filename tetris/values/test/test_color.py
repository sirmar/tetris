from nose.tools import istest, eq_, assert_raises
from tetris.values.color import Color, HeaderColor, MenuRowColor, MenuBackgroundColor

class TestColor(object):
    @istest
    def access_parts(self):
        c = Color(1, 5, 3, 0)
        eq_(c.r, 1)
        eq_(c.g, 5)
        eq_(c.b, 3)
        eq_(c.a, 0)

    @istest
    def same_color_is_equal(self):
        eq_(Color(0, 0, 0, 0), Color(0, 0, 0, 0))

    @istest
    def default_color_components_are_zero(self):
        eq_(Color(r=255), Color(255, 0, 0))
        eq_(Color(g=255), Color(0, 255, 0))
        eq_(Color(b=255), Color(0, 0, 255))

    @istest
    def default_alpha_component_are_zero(self):
        eq_(Color(), Color(0, 0, 0, 255))

    @istest
    def get_tuple(self):
        eq_(Color().tuple(), (0, 0, 0))

    @istest
    def range_check_colors(self):
        assert_raises(ValueError, Color, -1, 0, 0, 0)
        assert_raises(ValueError, Color, 0, -1, 0, 0)
        assert_raises(ValueError, Color, 0, 0, -1, 0)
        assert_raises(ValueError, Color, 0, 0, 0, -1)

        assert_raises(ValueError, Color, 256, 0, 0, 0)
        assert_raises(ValueError, Color, 0, 256, 0, 0)
        assert_raises(ValueError, Color, 0, 0, 256, 0)
        assert_raises(ValueError, Color, 0, 0, 0, 256)

    @istest
    def pre_defined_colors(self):
        eq_(HeaderColor(), Color(r=255))
        eq_(MenuRowColor(), Color(255, 255, 255))
        eq_(MenuBackgroundColor(), Color(50, 50, 50, 100))
