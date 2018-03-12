import attr


@attr.s
class Calculator():
    set_point = attr.ib()
    logger = attr.ib()

    def error_current(self):
        return self.logger.temperatures[-1] - self.set_point 
