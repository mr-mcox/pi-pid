import click
import time
import yaml
from .hardware.pi import Sensor, Switch
from .controller import controller
from .strategy import Relay, PID
from .calculator import Calculator
from .logger import Logger


@click.command()
@click.option('--mode', default='pid')
@click.option('--setpoint', default=60.0)
@click.option('--config', default=None)
@click.option('--logfile', default=None)
@click.option('--wait-time', default=10)
def cli(mode, setpoint, config, logfile, wait_time):
    conf = {'strategy': dict(),
            'logger': dict(),
            'calculator': dict()}
    if config is not None:
        with open(config) as fh:
            conf.update(yaml.load(fh))

    sensor = Sensor()
    switch = Switch()
    drop_thresh = setpoint - 1
    logger = Logger(file=logfile, sensor=sensor,
                    drop_after_crossing=drop_thresh,
                    **conf['logger'])
    calculator = Calculator(set_point=setpoint,
                            logger=logger, **conf['calculator'])
    strategy = None
    if mode == 'relay':
        strategy = Relay(calculator=calculator)
    elif mode == 'pid':
        strategy = PID(calculator, **conf['strategy'])

    try:
        while True:
            logger.record_sensor()
            lr = sensor.last_reading
            state = switch.state
            indicator = strategy.indicator
            print(f'\r{lr}°C State:{state} Ind:{indicator:.3f}')
            controller(switch=switch, strategy=strategy)
            time.sleep(wait_time)
    except KeyboardInterrupt:
        pass
    switch.cleanup()


if __name__ == '__main__':
    cli()
