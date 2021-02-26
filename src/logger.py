
import logging
from datetime import datetime
from typing import Optional


def setup(
    level_stream: Optional[int] = logging.DEBUG,
    level_file: Optional[int] = logging.DEBUG,
    filename: Optional[str] = datetime.now().strftime('%Y-%m-%d-%H:%M:%S') + '.log',
    fmt: Optional[str] = '[%(levelname)s: %(name)s: %(asctime)s] \n%(message)s',
    datefmt: Optional[str] = '%H:%M:%S',
    encoding: Optional[str] = 'utf-8') -> logging.Logger:
    """
    Examples:
        # 呼び出し先
        import logger
        logger = logger.setup()

        # 呼び出し元
        import logging
        logger = logging.getLoger(__name__)
    """
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(level=level_stream)
    ch.setFormatter(logging.Formatter('%(levelname)s: %(message)s'))
    logger.addHandler(ch)

    fh = logging.FileHandler(filename=filename, encoding=encoding)
    fh.setLevel(level_file)
    fh.setFormatter(logging.Formatter(fmt=fmt, datefmt=datefmt))
    logger.addHandler(fh)

    return logger


if __name__ == '__main__':
    logger = setup(level_stream=logging.WARNING)
    logger.debug('debug test')
    logger.info('info test')
    logger.warning('warning test')
    logger.error('error test')

