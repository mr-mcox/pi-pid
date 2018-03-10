import attr


@attr.s
class Sensor():

    reading = attr.ib(default=15.0)

    def read(self):
        return self.reading


@attr.s
class Switch():

    state = attr.ib(default='off')

    def set(self, state):
        self.state = state
