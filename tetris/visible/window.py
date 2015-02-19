"""
This class functions as root node in the scene graph.

Responsibilities:
- Clear the screen.
- Draw of the scene.
- Flip the buffers.
"""

from tetris.visible.composite import Composite

class Window(Composite):
    def __init__(self, display):
        Composite.__init__(self)
        self._display = display

    def surface(self):
        return self._display.get_surface()

    #pylint: disable=arguments-differ
    def draw(self):
        self._display.clear()
        Composite.draw(self, None)
        self._display.flip()
