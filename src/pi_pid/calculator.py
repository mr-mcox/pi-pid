import attr


@attr.s
class Calculator():
    set_point = attr.ib()
    logger = attr.ib()
    sensor = attr.ib()

    def error_current(self):
        self.logger.append(self.sensor.read())
        return self.logger.temperatures[-1] - self.set_point
