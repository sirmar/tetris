from mock import Mock
from nose.tools import istest

from tetris.wrappers.surface import Surface
from tetris.visibles.component import Component

#pylint: disable=attribute-defined-outside-init
class TestComponent(object):
    def setup(self):
        self.parent = Mock(Surface)
        self.component = Component()

    @istest
    def do_not_blit_without_surface(self):
        self.when_draw_is_called()
        self.then_do_not_blit()

    def when_draw_is_called(self):
        self.component.draw(self.parent)

    def then_do_not_blit(self):
        assert not self.parent.blit.called
