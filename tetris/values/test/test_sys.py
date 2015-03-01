from nose.tools import istest, eq_
from tetris.values.sys import Sys, Quit

class TestSys(object):

    @istest
    def same_sys_is_equal(self):
        eq_(Sys("sys"), Sys("sys"))

    @istest
    def sys_is_usable_as_key(self):
        sys_dict = {
            Sys("sys"): "Value"
        }
        eq_(sys_dict[Sys("sys")], "Value")

    @istest
    def predefined_sys(self):
        eq_(Quit(), Sys("Quit"))
