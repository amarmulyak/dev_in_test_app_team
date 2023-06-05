import subprocess
import time
import logging

import pytest
from appium import webdriver

from utilities.android_utils import android_get_desired_capabilities
from utilities.utils import get_path, get_root_folder


@pytest.fixture(scope='session')
def run_appium_server():
    subprocess.Popen(
        ['appium', '-a', '0.0.0.0', '-p', '4723', '--allow-insecure', 'adb_shell'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        stdin=subprocess.DEVNULL,
        shell=True
    )
    time.sleep(5)


@pytest.fixture(scope='session')
def driver(run_appium_server):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_capabilities())
    yield driver


def pytest_configure():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(funcName)s - %(levelname)s - %(message)s')

    debug_handler = logging.FileHandler(get_path(get_root_folder(), 'debug.log'), mode='w')
    debug_handler.setLevel(logging.DEBUG)
    debug_handler.setFormatter(formatter)
    logger.addHandler(debug_handler)

    info_handler = logging.FileHandler(get_path(get_root_folder(), 'info.log'), mode='w')
    info_handler.setLevel(logging.INFO)
    info_handler.setFormatter(formatter)
    logger.addHandler(info_handler)

    warning_handler = logging.FileHandler(get_path(get_root_folder(), 'warning.log'), mode='w')
    warning_handler.setLevel(logging.WARNING)
    warning_handler.setFormatter(formatter)
    logger.addHandler(warning_handler)
