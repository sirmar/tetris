"""
Container for visible components.

Responsibilities:
- Draw itself.
- Draw its children.
"""

from tetris.visibles.component import Component

class Composite(Component):
    def __init__(self):
        Component.__init__(self)
        self._children = []

    def add_child(self, child):
        self._children.append(child)

    def draw(self, parent):
        Component.draw(self, parent)
        for child in self._children:
            child.draw(self._surface)

    def remove_children(self):
        self._children = []
