"""
Abstract class representing any game state.
"""

class State(object):
    def __init__(self, window):
        self._window = window

    def init(self):
        self._window.remove_children()
        root = self.visibles()
        if root:
            self._window.add_child(root)
        return self

    #pylint: disable=unused-argument
    def handle(self, event):
        return self

    def update(self):
        return self

    def draw(self):
        self._window.draw()

    def visibles(self):
        return None
