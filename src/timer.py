
import time
from contextlib import contextmanager

@contextmanager
def timer(logger=None):
    """実行時間を測ってくれるコンテクストマネージャー

    Examples:
        with timer(logger):
            func()
    """
    t0 = time.time()
    yield
    if logger is not None:
        logger.info(f'done in {time.time() - t0:.0f} s')
    else:
        print(f'done in {time.time() - t0:.0f} s')


if __name__ == '__main__':
    with timer():
        time.sleep(2)
        print('aa')