class Engine(object):
    def __init__(self, pygame, window):
        self._pygame = pygame
        self._window = window
        self._running = True

    def start(self, width, height):
        self._window.open(width, height)
        self._loop()

    def _loop(self):
        self._pygame.write("Esc: Exit")
        while self._running:
            self._handle_keys()
            self._window.flip()
        self._pygame.quit()

    def _handle_keys(self):
        for key in self._pygame.get_keys():
            if key == "Escape":
                self.stop()

    def stop(self):
        self._running = False
