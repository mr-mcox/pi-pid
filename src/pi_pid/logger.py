import math
import attr
import time


@attr.s
class Logger():
    temperatures = attr.ib(default=list())
    times = attr.ib(default=list())
    max_len = attr.ib(default=math.inf)

    def append(self, temp=None):
        self.temperatures.append(temp)
        self.times.append(time.monotonic())
        if len(self.times) > self.max_len:
            self.temperatures.pop(0)
            self.times.pop(0)
