#pylint: disable=W0201

from mock import Mock
from nose.tools import istest
from tetris.wrapper.surface import Surface

from tetris.visible.component import Component

class TestComponent(object):
    def setup(self):
        self.parent = Mock(Surface)
        self.child = Mock(Surface)
        self.component = Component(self.child)

    @istest
    def default_position_is_zero(self):
        self.when_draw_is_called()
        self.then_blit_surface_on_parent_on_position((0, 0))

    @istest
    def blit_surface_on_parent(self):
        self.given_a_surface_with_position((10, 20))
        self.when_draw_is_called()
        self.then_blit_surface_on_parent_on_position((10, 20))

    def given_a_surface_with_position(self, position):
        self.component.set_position(position)

    def when_draw_is_called(self):
        self.component.draw(self.parent)

    def then_blit_surface_on_parent_on_position(self, position):
        self.parent.blit.assert_called_once_with(self.child, position)
