from .shared_bool import SharedBool
from .quicklogger_out_group import QuickLoggerOutGroup
import threading


class QuickLoggerGroup(QuickLoggerOutGroup):
    def __init__(self):
        super().__init__()

        self.loggers = []
        self._enabled = SharedBool(True)
        self._lock = threading.Lock()

    def add_logger(self, logger):
        logger.outs = [self]
        logger.enabled = self._enabled
        logger.lock = self._lock
        self.loggers.append(logger)

    def enable(self):
        self._enabled.value = True

    def disable(self):
        self._enabled.value = False

