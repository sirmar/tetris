"""
Base class for all nodes in the scene graph. It is implemented
using the composite pattern.

Responsibilities:
- Hold the relative position to its parent.
- Blit itself on the parent.
- Dirty flag itself to trigger regeneration of surface.
"""

class Component(object):
    def __init__(self):
        self._position = (0, 0)
        self._dirty = True
        self._surface = None

    def draw(self, parent):
        self._redo_dirty_surface()
        if self._surface and parent:
            parent.blit(self._surface, self._position)

    def set_position(self, position):
        self._position = position

    def surface(self):
        return None

    def dirty(self):
        self._dirty = True

    def _redo_dirty_surface(self):
        if self._dirty:
            self._surface = self.surface()
            self._dirty = False

"""
Decorator to mark component methods that change the look
of the surface and therefor need to trigger regeneration.
"""
def dirty(function):
    def wrapper(self, *args):
        self.dirty()
        return function(self, *args)
    return wrapper
