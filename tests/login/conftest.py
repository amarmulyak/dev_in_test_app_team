import pytest

from framework.page_objects import LoginPage, PopupModal


@pytest.fixture(scope='function')
def user_login_fixture(driver):
    yield LoginPage(driver)

@pytest.fixture(scope='function')
def popup_fixture(driver):
    yield PopupModal(driver)