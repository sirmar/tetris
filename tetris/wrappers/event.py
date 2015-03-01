from pygame import KEYUP, K_ESCAPE, QUIT
from pygame.event import Event as PyEvent
from pygame.event import post

class Event(object):
    def __init__(self, event):
        self.event = event

    def _key_up(self):
        return self.event.type == KEYUP

    def _is_key(self, key):
        if self._key_up():
            return self.event.key == key

    def escape(self):
        return self._is_key(K_ESCAPE)

    def letter(self, letter):
        return self._is_key(ord(letter))

    def number(self, number):
        return self._is_key(int(number) + 48)

    def quit(self):
        return self.event.type == QUIT

    @staticmethod
    def send_quit_event():
        post(PyEvent(QUIT))
