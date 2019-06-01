import sys
import traceback
from ..quicklogger import QuickLogger
from ..quicklogger_group import QuickLoggerGroup


class DefaultLoggingTemplate(QuickLoggerGroup):
    def __init__(self):
        super().__init__()

        self.log_error = QuickLogger()
        self.log_error.prefix = lambda: ('[ERROR]',)

        self.log_info = QuickLogger()
        self.log_info.prefix = lambda: ('[INFO]',)

        self.log_raw = QuickLogger()
        self.log_raw.parts = lambda *args, **kwargs: (
            *args,
            *(kwargs.items())
        )

        self.add_logger(self.log_info)
        self.add_logger(self.log_error)
        self.add_logger(self.log_raw)

    def log_exception(self, *exc_info):
        if self._enabled:
            self.log_error(
                ''.join(traceback.format_exception(*exc_info))
            )
        else:
            sys.__excepthook__(*exc_info)

    def intercept_except_hook(self):
        sys.excepthook = self.log_exception
