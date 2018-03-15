from pi_pid.logger import Logger
from pi_pid.calculator import Calculator
from pi_pid.hardware.mock import Sensor


def test_error_current():
    sensor = Sensor()
    logger = Logger(sensor=sensor)
    sensor.reading = 14
    logger.record_sensor()
    calc = Calculator(set_point=15, logger=logger)
    assert calc.error_current() == -1
