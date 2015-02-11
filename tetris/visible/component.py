"""
Base class for all nodes in the scene graph. It is implemented
using the composite pattern.

Responsibilities:
- Hold the relative position to its parent.
- Blit itself on the parent.
"""

class Component(object):
    def __init__(self, surface):
        self._surface = surface
        self.set_position((0, 0))

    def draw(self, parent):
        parent.blit(self._surface, self._position)

    def set_position(self, position):
        self._position = position
