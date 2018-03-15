from src.pi_pid.logger import Logger


def test_updated_on_append():
    logger = Logger()
    assert len(logger.temperatures) == 0
    assert len(logger.times) == 0
    logger.append(temp=1.0)
    assert len(logger.temperatures) == 1
    assert len(logger.times) == 1


def test_max_length():
    logger = Logger(max_len=3)
    for x in range(10):
        logger.append(temp=x)
        assert len(logger.temperatures) <= 3
        assert logger.temperatures[-1] == x


def test_drop_after_crossing():
    logger = Logger(drop_after_crossing=5)
    for x in range(10):
        logger.append(temp=x)
    assert logger.temperatures.min() >= 5
