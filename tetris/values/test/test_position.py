#pylint: disable=W0201,C0103

from nose.tools import istest, eq_, ok_
from tetris.values.position import Position

class TestPosition(object):
    @istest
    def same_point_is_equal(self):
        eq_(Position(0, 0), Position(0, 0))

    @istest
    def check_types(self):
        class Pos(object):
            def __init__(self, x, y):
                self.x = x
                self.y = y

        ok_(Position(0, 0) != Pos(0, 0))
