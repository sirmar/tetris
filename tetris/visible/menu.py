from tetris.visible.composite import Composite
from tetris.wrapper.surface import Surface
from tetris.visible.component import dirty

class Menu(Composite):
    def __init__(self, factory):
        Composite.__init__(self)
        self._factory = factory
        self._header = None
        self._y_position = 0

    @dirty
    def set_header(self, text):
        if not self._header:
            self._header = self._factory.create_header()
            self.add_child(self._header)
            self._y_position += self._header.get_font_size()
        self._header.set_text(text)

    @dirty
    def add_row(self, text=""):
        if len(text) > 0:
            row = self._factory.create_menu_row()
            row.set_text(text)
            row.set_position((0, self._y_position))
            self._y_position += row.get_font_size()
            self.add_child(row)
        else:
            self._y_position += 10


    def surface(self):
        surface = Surface.create((300, self._y_position))
        surface.fill((50, 50, 50))
        return surface
