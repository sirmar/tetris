"""
Composite that holds headers, menu items and a background to
create an in game menu.
"""

from tetris.visibles.composite import Composite
from tetris.wrappers.surface import Surface
from tetris.visibles.component import recreate_surface
from tetris.values.color import MenuBackgroundColor
from tetris.values.position import Position
from tetris.values.size import Size

class Menu(Composite):
    def __init__(self, factory):
        Composite.__init__(self)
        self._factory = factory
        self._cursor_position = Position(10, 10)

    @recreate_surface
    def add_header(self, text):
        header = self._factory.create_header()
        self._add_row(header, text)

    @recreate_surface
    def add_choice(self, text):
        choice = self._factory.create_menu_row()
        self._add_row(choice, text)

    @recreate_surface
    def add_space(self):
        self._cursor_position = self._cursor_position.down(10)

    def surface(self):
        size = Size(300, self._cursor_position.y + 10)
        surface = Surface.create(size)
        surface.fill(MenuBackgroundColor())
        return surface

    def _move_cursor_by_font_size(self, text):
        font_size = text.get_font_size()
        self._cursor_position = self._cursor_position.down(font_size)

    def _add_row(self, element, text):
        element.set_position(self._cursor_position)
        element.set_text(text)
        self._move_cursor_by_font_size(element)
        self.add_child(element)
