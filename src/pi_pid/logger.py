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
    drop_after_crossing = attr.ib(default=math.inf)
    file = attr.ib(default=None)

    def __attrs_post_init__(self):
        if self.file is not None:
            with open(self.file, 'w') as fh:
                fh.write('time,temperature\n')

        if self.drop_after_crossing < math.inf:
            self.drop_after_crossing_armed = True
        else:
            self.drop_after_crossing_armed = False

    def record_sensor(self):
        self.append(temp=self.sensor.read())

    def apply_drop_after_crossing(self, temp):
        thresh = self.drop_after_crossing
        if temp > thresh:
            drop_before = np.argmax(self.temperatures > thresh)
            self.temperatures = self.temperatures[drop_before:]
            self.times = self.times[drop_before:]

    def apply_max_len(self):
        if len(self.times) > self.max_len:
            self.temperatures = self.temperatures[1:]
            self.times = self.times[1:]

    def append(self, temp=None):
        cur_time = time.monotonic()
        self.temperatures = np.append(self.temperatures, [temp])
        self.times = np.append(self.times, [cur_time])
        if self.file is not None:
            with open(self.file, 'a') as fh:
                fh.write(f'{cur_time},{temp}\n')

        self.apply_max_len()

        if self.drop_after_crossing_armed:
            self.apply_drop_after_crossing(temp)
