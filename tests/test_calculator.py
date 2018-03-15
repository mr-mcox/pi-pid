from pi_pid.logger import Logger
from pi_pid.calculator import Calculator
from pi_pid.hardware.mock import Sensor
import numpy as np


def test_error_current():
    sensor = Sensor()
    logger = Logger(sensor=sensor)
    sensor.reading = 14
    logger.record_sensor()
    calc = Calculator(set_point=15, logger=logger)
    assert calc.error_current() == -1


def test_error_derivative():
    logger = Logger()
    logger.temperatures = np.array([1, 3, 7])
    logger.times = np.arange(3)
    calc = Calculator(logger=logger, deriv_lookback=2)
    assert calc.error_derivative() == 3


def test_error_derivative_when_short():
    logger = Logger()
    logger.temperatures = np.array([1, 3, 7])
    logger.times = np.arange(3)
    calc = Calculator(logger=logger, deriv_lookback=5)
    assert calc.error_derivative() == 0


def test_integral():
    logger = Logger()
    temps = np.array([1, 3, 7])
    logger.temperatures = temps
    logger.times = np.arange(3)
    calc = Calculator(logger=logger, set_point=0)
    exp_integral = np.sum(temps[1:] + temps[:-1]) / 2
    assert calc.error_integral() == exp_integral


def test_integral_short():
    logger = Logger()
    temps = np.array([23])
    logger.temperatures = temps
    logger.times = np.array([5])
    calc = Calculator(logger=logger)
    assert calc.error_integral() == 0
