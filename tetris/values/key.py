"""
Represents a keyboard button
"""

class Key(object):
    def __init__(self, key):
        self.key = key

    def __eq__(self, other):
        return isinstance(other, Key) and self.key == other.key

    def __hash__(self):
        return hash(self.key)

    def __repr__(self):
        return "Key(%s)" % (self.key)
