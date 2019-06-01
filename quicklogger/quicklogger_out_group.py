from typing import TYPE_CHECKING, Iterable

if TYPE_CHECKING:
    from io import TextIOWrapper


class QuickLoggerOutGroup:
    def __init__(self):
        self.outs: Iterable[TextIOWrapper] = []

    def write(self, data):
        for out in self.outs:
            out.write(data)

    def flush(self):
        for out in self.outs:
            out.flush()
