import sys
from quicklogger.templates import DefaultLoggingTemplate

lg = DefaultLoggingTemplate()
lg.intercept_except_hook()
lg.outs = (
    sys.stderr,
    open('default.log', 'a'),
)

lg.log_info('Random info.')
