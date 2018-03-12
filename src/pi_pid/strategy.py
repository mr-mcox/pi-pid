import attr


@attr.s
class Relay():
    calculator = attr.ib()
    noise_thresh = attr.ib(default=0.15)

    def evaluate(self):
        error_current = self.calculator.error_current()
        if error_current < -1 * self.noise_thresh:
            return 'on'
        elif error_current > self.noise_thresh:
            return 'off'
        else:
            return 'no_change'
