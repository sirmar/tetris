from pygame import KEYDOWN, QUIT, K_ESCAPE
from pygame import event as py_events
from pygame.event import Event as PyEvent
from tetris.values.key import Key
from tetris.values.sys import Quit

class Event(object):
    def receive(self):
        events = []
        for event in py_events.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    events.append(Key("Esc"))
                else:
                    events.append(Key(event.unicode))
            if event.type == QUIT:
                events.append(Quit())
        return events

    @staticmethod
    def send_quit():
        py_events.post(PyEvent(QUIT))
