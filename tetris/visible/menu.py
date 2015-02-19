"""
Composite that holds headers, menu items and a background to
create an in game menu.

Responsibilities:
- Create and draw menus
"""

from tetris.visible.composite import Composite
from tetris.wrapper.surface import Surface
from tetris.visible.component import recreate_surface
from tetris.values.color import MenuBackgroundColor
from tetris.values.position import Position
from tetris.values.size import Size

class Menu(Composite):
    def __init__(self, factory):
        Composite.__init__(self)
        self._factory = factory
        self._cursor_position = Position(10, 10)

    @recreate_surface
    def set_header(self, text):
        header = self._factory.create_header()
        header.set_position(self._cursor_position)
        self.add_child(header)
        self._move_cursor_by_font_size(header)
        header.set_text(text)

    @recreate_surface
    def add_row(self, text=""):
        if len(text) > 0:
            row = self._factory.create_menu_row()
            row.set_text(text)
            row.set_position(self._cursor_position)
            self._move_cursor_by_font_size(row)
            self.add_child(row)
        else:
            self._cursor_position = self._cursor_position.down(10)

    def _move_cursor_by_font_size(self, text):
        font_size = text.get_font_size()
        self._cursor_position = self._cursor_position.down(font_size)

    def surface(self):
        size = Size(300, self._cursor_position.y + 10)
        surface = Surface.create(size)
        surface.fill(MenuBackgroundColor())
        return surface
