import attr
from pi_pid.strategy import Relay


@attr.s
class MockCalculator():
    error = attr.ib(default=0)

    def error_current(self):
        return self.error


def test_relay_on_when_low():
    calc = MockCalculator()
    strat = Relay(noise_thresh=1, calculator=calc)
    calc.error = -5
    assert strat.evaluate() == 'on'


def test_relay_off_when_high():
    calc = MockCalculator()
    strat = Relay(noise_thresh=1, calculator=calc)
    calc.error = 5
    assert strat.evaluate() == 'off'


def test_relay_no_change():
    calc = MockCalculator()
    strat = Relay(noise_thresh=1, calculator=calc)
    calc.error = 0
    assert strat.evaluate() == 'no_change'
