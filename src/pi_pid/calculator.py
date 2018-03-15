import attr
import numpy as np


@attr.s
class Calculator():
    logger = attr.ib()
    set_point = attr.ib(default=60)
    deriv_lookback = attr.ib(default=30)

    def error_current(self):
        return self.logger.temperatures[-1] - self.set_point

    def error_derivative(self):
        times = self.logger.times
        temps = self.logger.temperatures
        lookback_time = times[-1] - self.deriv_lookback
        i = np.argmax(times > lookback_time) - 1
        if i < 0:
            return 0
        deriv = (temps[-1] - temps[i]) / (times[-1] - times[i])
        return deriv

    def error_integral(self):
        times = self.logger.times
        temps = self.logger.temperatures
        heights = (temps[1:] + temps[:-1]) / 2
        widths = times[1:] - times[:-1]
        return np.sum(heights * widths)
