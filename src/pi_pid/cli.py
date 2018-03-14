import click
import time
from .hardware.pi import Sensor, Switch
from .controller import controller
from .strategy import Relay
from .calculator import Calculator
from .logger import Logger


@click.command()
@click.option('--setpoint', default=60.0)
@click.option('--logfile', default=None)
def cli(setpoint, logfile):
    sensor = Sensor()
    switch = Switch()
    logger = Logger(file=logfile)
    calculator = Calculator(set_point=setpoint, sensor=sensor, logger=logger)
    relay = Relay(calculator=calculator)
    for x in range(10):
        sensor.reading = x
        print(switch.state)
        controller(switch=switch, strategy=relay)
        time.sleep(1)


if __name__ == '__main__':
    cli()
