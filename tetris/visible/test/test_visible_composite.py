#pylint: disable=W0201

from mock import Mock
from nose.tools import istest
from tetris.wrapper.surface import Surface
from tetris.visible.component import Component
from tetris.visible.composite import Composite

class TestVisibleComposite(object):
    def setup(self):
        self.surface = Mock(Surface)
        self.composite = Composite(self.surface)

    @istest
    def default_position_is_zero(self):
        self.when_draw_is_called()
        self.then_blit_surface_on_parent_on_position((0, 0))

    @istest
    def draw_children(self):
        self.given_children()
        self.when_draw_is_called()
        self.then_draw_all_children()

    def given_children(self):
        self.child1 = Mock(Component)
        self.child2 = Mock(Component)
        self.composite.add_child(self.child1)
        self.composite.add_child(self.child2)

    def when_draw_is_called(self):
        self.parent = Mock(Surface)
        self.composite.draw(self.parent)

    def then_blit_surface_on_parent_on_position(self, position):
        self.parent.blit.assert_called_once_with(self.surface, position)

    def then_draw_all_children(self):
        self.child1.draw.assert_called_once_with(self.composite)
        self.child2.draw.assert_called_once_with(self.composite)
