import functools
import os
import random
import string
import time
from pathlib import Path

from faker import Faker

from config import TIMEOUT, POLLING

fake = Faker()


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


def get_random_string(num: int = 5,
                      ascii_lowercase: bool = True,
                      ascii_uppercase: bool = False,
                      digits: bool = True,
                      punctuation: bool = False):
    characters = str()

    if ascii_lowercase:
        characters += string.ascii_lowercase
    if ascii_uppercase:
        characters += string.ascii_uppercase
    if digits:
        characters += string.digits
    if punctuation:
        characters += string.punctuation

    return ''.join(random.choices(characters, k=num))


def get_root_folder() -> Path:
    return Path(__file__).parent.parent.absolute()


def get_path(*path) -> str:
    return os.path.join(get_root_folder(), *path)
