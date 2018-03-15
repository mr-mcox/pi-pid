import math
import attr
import time


@attr.s
class Logger():
    sensor = attr.ib(default=None)
    temperatures = attr.ib(default=list())
    times = attr.ib(default=list())
    max_len = attr.ib(default=math.inf)
    file = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.file is not None:
            with open(self.file, 'w') as fh:
                fh.write('time,temperature\n')

    def record_sensor(self):
        self.append(temp=self.sensor.read())

    def append(self, temp=None):
        cur_time = time.monotonic()
        self.temperatures.append(temp)
        self.times.append(cur_time)
        if self.file is not None:
            with open(self.file, 'a') as fh:
                fh.write(f'{cur_time},{temp}\n')
        if len(self.times) > self.max_len:
            self.temperatures.pop(0)
            self.times.pop(0)
