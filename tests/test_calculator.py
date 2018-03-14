from pi_pid.logger import Logger
from pi_pid.calculator import Calculator
from pi_pid.hardware.mock import Sensor


def test_error_current():
    logger = Logger()
    sensor = Sensor()
    sensor.reading = 14
    calc = Calculator(set_point=15, logger=logger, sensor=sensor)
    assert calc.error_current() == -1
