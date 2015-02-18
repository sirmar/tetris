"""
Wraps a pygame surface.
"""

from pygame import Surface as PySurface

class Surface(object):
    def __init__(self, surface):
        self.surface = surface

    def blit(self, source, position):
        self.surface.blit(source.surface, position)

    def fill(self, color):
        self.surface.fill(color)

    @staticmethod
    def create(size):
        return Surface(PySurface(size))
