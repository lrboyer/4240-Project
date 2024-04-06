import time


class Stopwatch:
    def __init__(self):
        self._start_time = None
        self._elapsed_time = 0

    def start(self):
        if self._start_time is not None:
            raise RuntimeError("Stopwatch is already running")
        self._start_time = time.time()

    def stop(self):
        if self._start_time is None:
            raise RuntimeError("Stopwatch is not running")
        elapsed = time.time() - self._start_time
        self._elapsed_time += elapsed
        self._start_time = None

    def reset(self):
        self._start_time = None
        self._elapsed_time = 0

    def elapsed_time(self):
        if self._start_time is None:
            return self._elapsed_time
        else:
            return self._elapsed_time + (time.time() - self._start_time)
