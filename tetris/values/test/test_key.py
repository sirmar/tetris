from nose.tools import istest, eq_
from tetris.values.key import Key

class TestKey(object):

    @istest
    def same_key_is_equal(self):
        eq_(Key("key"), Key("key"))

    @istest
    def key_is_usable_as_key(self):
        key_dict = {
            Key("key"): "Value"
        }
        eq_(key_dict[Key("key")], "Value")
