from pygame import event
from tetris.wrappers.event import Event

class EventQueue(object):
    def events(self):
        return [Event(e) for e in event.get()]
