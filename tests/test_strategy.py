import attr
import pytest
from pi_pid.strategy import Relay, PID


@attr.s
class MockCalculator():
    err_current = attr.ib(default=0)
    err_deriv = attr.ib(default=0)
    err_integral = attr.ib(default=0)

    def error_current(self):
        return self.err_current

    def error_derivative(self):
        return self.err_deriv

    def error_integral(self):
        return self.err_integral


@pytest.mark.parametrize('error,output',
                         [(-5, 'on'),
                          (5, 'off'),
                             (0, 'no_change')])
def test_relay(error, output):
    calc = MockCalculator()
    strat = Relay(noise_thresh=1, calculator=calc)
    calc.err_current = error
    assert strat.evaluate() == output


@pytest.mark.parametrize('error,output',
                         [(-5, 'on'),
                          (5, 'off'),
                             (0, 'no_change')])
def test_pid_noise_thresh(error, output):
    calc = MockCalculator()
    strat = PID(kp=1, calculator=calc, noise_thresh=1)
    calc.err_current = error
    assert strat.evaluate() == output


def test_pid_kd():
    calc = MockCalculator()
    strat = PID(kd=1, calculator=calc, noise_thresh=1)
    calc.err_deriv = 5
    assert strat.evaluate() == 'off'


def test_pid_ki():
    calc = MockCalculator()
    strat = PID(ki=1, calculator=calc, noise_thresh=1)
    calc.err_integral = 5
    assert strat.evaluate() == 'off'
