import attr


@attr.s
class Relay():
    calculator = attr.ib()
    noise_thresh = attr.ib(default=0.15)
    indicator = attr.ib(default=0)

    def evaluate(self):
        error_current = self.calculator.error_current()
        if error_current < -1 * self.noise_thresh:
            return 'on'
        elif error_current > self.noise_thresh:
            return 'off'
        else:
            return 'no_change'


@attr.s
class PID():
    calculator = attr.ib()
    kp = attr.ib(default=0)
    kd = attr.ib(default=0)
    ki = attr.ib(default=0)
    indicator = attr.ib(default=0)
    noise_thresh = attr.ib(default=0.05)

    def evaluate(self):
        calc = self.calculator
        indicator = (calc.error_current() * self.kp
                     + calc.error_derivative() * self.kd
                     + calc.error_integral() * self.ki)
        self.indicator = indicator
        if indicator < -1 * self.noise_thresh:
            return 'on'
        elif indicator > self.noise_thresh:
            return 'off'
        else:
            return 'no_change'
