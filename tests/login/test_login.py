import pytest

from config import EMAIL, PASSWORD
from utils.utils import get_random_string, fake
from framework.test_data.error_messages import ErrorMessages


@pytest.fixture(scope='module')
def open_login_page(user_login_fixture):
    user_login_fixture \
        .click_main_login_button() \
        .verify_page_is_opened()


def test_user_login(user_login_fixture, popup_fixture, home_fixture):
    user_login_fixture \
        .click_main_login_button() \
        .input_email(EMAIL) \
        .input_password(PASSWORD) \
        .click_login_button()

    popup_fixture \
        .click_deny_button()

    home_fixture \
        .verify_page_is_opened()


@pytest.mark.parametrize('email, password, error',
                         [
                             (EMAIL, get_random_string(), ErrorMessages.WRONG_LOGIN_PASSWORD),
                             (fake.email(), PASSWORD, ErrorMessages.WRONG_LOGIN_PASSWORD),
                             (get_random_string(), PASSWORD, ErrorMessages.INVALID_EMAIL_FORMAT)
                         ],
                         ids=[
                             'Correct email, incorrect password',
                             'Incorrect email, correct password',
                             'Random string as email, correct password'
                         ]
                         )
def test_user_login_negative(user_login_fixture, open_login_page, email, password, error):
    error_message = user_login_fixture \
        .input_email(email) \
        .input_password(password) \
        .click_login_button() \
        .get_notification_error_text()

    user_login_fixture \
        .verify_page_is_opened()

    assert error_message == error.value
