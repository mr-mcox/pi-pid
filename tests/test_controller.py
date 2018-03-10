import attr
from pi_pid.hardware.mock import Sensor, Switch
from pi_pid.controller import controller


@attr.s
class SimpleStrategy():

    sensor = attr.ib()

    def evaluate(self):
        if self.sensor.read() > 0:
            return 'on'
        else:
            return 'off'


def test_on_when_high():
    sense = Sensor()
    strat = SimpleStrategy(sensor=sense)
    switch = Switch()
    controller(switch, strategy=strat)
    assert switch.state == 'ON'

def test_off_when_low():
    sense = Sensor()
    sense.reading = 0
    strat = SimpleStrategy(sensor=sense)
    switch = Switch()
    controller(switch, strategy=strat)
    assert switch.state == 'OFF'
