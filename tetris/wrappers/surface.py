"""
Wraps a pygame surface.
"""

class Surface(object):
    def __init__(self, surface):
        self.surface = surface

    def blit(self, source, position):
        self.surface.blit(source.surface, position)
