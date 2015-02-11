from pygame import KEYUP, K_ESCAPE

class Event(object):
    def __init__(self, event):
        self.event = event

    def _key_up(self):
        return self.event.type == KEYUP

    def _is_key(self, key):
        return self._key_up() and self.event.key == key

    def escape(self):
        return self._is_key(K_ESCAPE)
