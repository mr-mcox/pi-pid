import math
import attr
import time
import numpy as np


@attr.s
class Logger():
    sensor = attr.ib(default=None)
    temperatures = attr.ib(default=np.array(list()))
    times = attr.ib(default=np.array(list()))
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
        self.temperatures = np.append(self.temperatures, [temp])
        self.times = np.append(self.times, [cur_time])
        if self.file is not None:
            with open(self.file, 'a') as fh:
                fh.write(f'{cur_time},{temp}\n')
        if len(self.times) > self.max_len:
            self.temperatures = self.temperatures[1:]
            self.times = self.times[1:]
