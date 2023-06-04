import functools
import time

from config import TIMEOUT, POLLING


def retry(timeout=TIMEOUT, polling=POLLING):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            end_time = time.time() + timeout
            while True:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if time.time() > end_time:
                        raise e
                    time.sleep(polling)

        return wrapper

    return decorator
