from nose.tools import istest, eq_, ok_
from tetris.values.position import Position

#pylint: disable=invalid-name
class TestPosition(object):
    @istest
    def access_parts(self):
        p = Position(1, 5)
        eq_(p.x, 1)
        eq_(p.y, 5)

    @istest
    def same_point_is_equal(self):
        eq_(Position(0, 0), Position(0, 0))

    @istest
    def check_types_to_be_equal(self):
        class Pos(object):
            def __init__(self, x, y):
                self.x = x
                self.y = y
        ok_(Position(0, 0) != Pos(0, 0))

    @istest
    def add(self):
        eq_(Position(1, 1), Position(0, 0) + Position(1, 1))

    @istest
    def move(self):
        eq_(Position(2, 3), Position(0, 0).move(2, 3))

    @istest
    def move_right(self):
        eq_(Position(2, 0), Position(0, 0).right(2))
        eq_(Position(1, 0), Position(0, 0).right())

    @istest
    def move_left(self):
        eq_(Position(0, 0), Position(2, 0).left(2))
        eq_(Position(0, 0), Position(1, 0).left())

    @istest
    def move_down(self):
        eq_(Position(0, 2), Position(0, 0).down(2))
        eq_(Position(0, 1), Position(0, 0).down())

    @istest
    def move_up(self):
        eq_(Position(0, 0), Position(0, 2).up(2))
        eq_(Position(0, 0), Position(0, 1).up())

    def get_tuple(self):
        eq_(Position(0, 0).tuple(), (0, 0))
