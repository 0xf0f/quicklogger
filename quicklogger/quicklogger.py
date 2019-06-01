import sys
import datetime
import threading


class QuickLogger:
    def __init__(self):
        self.enabled = True
        self.outs = [sys.stderr]
        self.lock = threading.Lock()

    def prefix(self):
        yield from ()

    def suffix(self):
        yield from ()

    def body(self, *args, **kwargs):
        yield from args
        yield from kwargs.items()

    def timestamp(self):
        yield f'[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]'

    def parts(self, *args, **kwargs):
        yield from self.timestamp()
        yield from self.prefix()
        yield from self.body(*args, **kwargs)
        yield from self.suffix()

    def __call__(self, *args, **kwargs):
        if self.enabled:
            with self.lock:
                for out in self.outs:
                    print(
                        *self.parts(*args, **kwargs), file=out
                    )
