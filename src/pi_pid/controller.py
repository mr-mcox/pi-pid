def controller(switch, strategy):
    strategy_result = strategy.evaluate()
    if strategy_result == 'on':
        switch.set('ON')
    else:
        switch.set('OFF')
