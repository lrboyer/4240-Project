from typing import TextIO


class Logger:

    def log(self,
            *values,
            sep: str | None = " ",
            end: str | None = "\n",
            file: TextIO | None = None):
        print(*values, sep=sep, end=end)


class VoidLogger(Logger):
    def log(self,
            *values,
            sep: str | None = " ",
            end: str | None = "\n"):
        pass
