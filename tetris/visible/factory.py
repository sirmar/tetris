from tetris.visible.text import Text
from tetris.visible.header import Header
from tetris.visible.menu_row import MenuRow
from tetris.visible.menu import Menu

class Factory(object):
    def __init__(self, font):
        self._font = font

    def create_text(self):
        return Text(self._font)

    def create_header(self):
        return Header(self._font)

    def create_menu_row(self):
        return MenuRow(self._font)

    def create_menu(self):
        return Menu(self)
