from mock import Mock
from nose.tools import istest

from tetris.visibles.component import Component
from tetris.visibles.composite import Composite

#pylint: disable=attribute-defined-outside-init
class TestComposite(object):
    def setup(self):
        self.composite = Composite()

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
        self.composite.draw(None)

    def then_draw_all_children(self):
        self.child1.draw.assert_called_once_with(None)
        self.child2.draw.assert_called_once_with(None)