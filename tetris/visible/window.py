"""
This class functions as root node in the scene graph.

Responsibilities:
- Clear the screen.
- Draw of the scene.
- Flip the buffers.
"""

class Window(object):
    def __init__(self, display):
        self._display = display
        self.children = []

    def draw(self):
        root = self._display.get_surface()
        for child in self.children:
            root.blit(child, (0, 0))
        self._display.flip()

    def add_child(self, child):
        self.children.append(child)
