from .shared_bool import SharedBool
import threading


class QuickLoggerGroup:
    def __init__(self):
        self.loggers = []
        self.outs = []
        self._enabled = SharedBool(True)
        self._lock = threading.Lock()

    def add_logger(self, logger):
        logger.outs = self.outs
        logger.enabled = self._enabled
        logger.lock = self._lock
        self.loggers.append(logger)

    def enable(self):
        self._enabled.value = True

    def disable(self):
        self._enabled.value = False
