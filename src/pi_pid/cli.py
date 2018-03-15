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
@click.option('--wait-time', default=10)
def cli(setpoint, logfile, wait_time):
    sensor = Sensor()
    switch = Switch()
    logger = Logger(file=logfile, sensor=sensor)
    calculator = Calculator(set_point=setpoint, logger=logger)
    relay = Relay(calculator=calculator)
    try:
        while True:
            logger.record_sensor()
            lr = sensor.last_reading
            state = switch.state
            error = calculator.error_current()
            print(f'\r{lr}°C State:{state} Error: {error}')
            controller(switch=switch, strategy=relay)
            time.sleep(wait_time)
    except KeyboardInterrupt:
        pass
    switch.cleanup()


if __name__ == '__main__':
    cli()
