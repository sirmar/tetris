"""
Container for visible components and itself a visible component.
"""

from tetris.visible.component import Component

class Composite(Component):
    def __init__(self, surface):
        Component.__init__(self, surface)
        self._children = []

    def add_child(self, child):
        self._children.append(child)

    def draw(self, parent):
        Component.draw(self, parent)
        for child in self._children:
            child.draw(self)
