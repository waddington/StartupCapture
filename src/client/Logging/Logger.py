import logging
import os

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'))


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(os.environ.get('LOGLEVEL', 'INFO'))
    logger.addHandler(handler)
    return logger
