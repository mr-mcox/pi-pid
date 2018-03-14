import attr
import os
import time
import RPi.GPIO as io


@attr.s
class Sensor():

    reading = attr.ib(default=15.0)

    def __init__(self):
        os.system('modprobe w1-gpio')
        os.system('modprobe w1-therm')

        self.device_file = '/sys/bus/w1/devices/28-000004f117ea/w1_slave'

    def read_probe(self):
        with open(self.device_file) as s:
            return s.readlines()

    def read(self):
        # todo I suspect that this should be tested and refactored
        lines = self.read_probe()
        while lines[0].strip()[-3:] != 'YES':
            time.sleep(0.2)
            lines = self.read_probe()
        equals_pos = lines[1].find('t=')
        assert equals_pos != -1
        temp_string = lines[1][equals_pos + 2:]
        temp_c = temp_string / 1000.0
        return temp_c


@attr.s
class Switch():

    state = attr.ib(default='off')

    def __init__(self):
        # Set up power
        io.setmode(io.BCM)
        power_pin = 23
        io.setup(power_pin, io.OUT)
        io.output(power_pin, False)
        self.state = "OFF"
        self.power_pin = power_pin

    def set(self, state):
        self.state = state
        if state == 'ON':
            io.output(self.power_pin, True)
        elif state == 'OFF':
            io.output(self.power_pin, False)
