#pylint: disable=W0201

from mock import Mock
from nose.tools import istest
from tetris.wrapper.surface import Surface

from tetris.visible.component import Component

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
