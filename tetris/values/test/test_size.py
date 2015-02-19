from nose.tools import istest, eq_, assert_raises
from tetris.values.size import Size, BlockSize

#pylint: disable=invalid-name
class TestSize(object):
    @istest
    def access_parts(self):
        p = Size(1, 5)
        eq_(p.width, 1)
        eq_(p.height, 5)

    @istest
    def same_size_is_equal(self):
        eq_(Size(1, 1), Size(1, 1))

    @istest
    def get_tuple(self):
        eq_(Size(1, 1).tuple(), (1, 1))

    @istest
    def range_check_sizes(self):
        assert_raises(ValueError, Size, 0, 1)
        assert_raises(ValueError, Size, 1, 0)

    @istest
    def block_size_is_ten(self):
        eq_(BlockSize(), Size(10, 10))
