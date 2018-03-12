from pi_pid.logger import Logger
from pi_pid.calculator import Calculator


def test_error_current():
    logger = Logger()
    calc = Calculator(set_point=15, logger=logger)
    logger.append(temp=14)
    assert calc.error_current() == -1
