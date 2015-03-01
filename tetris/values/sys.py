"""
Represents a system event
"""

#pylint: disable=invalid-name
class Sys(object):
    def __init__(self, sys):
        self.sys = sys

    def __eq__(self, o):
        return isinstance(o, Sys) and self.sys == o.sys

    def __hash__(self):
        return hash(self.sys)

    def __repr__(self):
        return "Sys(%s)" % (self.sys)

class Quit(Sys):
    def __init__(self):
        Sys.__init__(self, "Quit")
