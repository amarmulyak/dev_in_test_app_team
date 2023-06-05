import logging

import pytest

from config import EMAIL, PASSWORD
from utilities.utils import get_random_string, fake
from framework.test_data.error_messages import ErrorMessages

logger = logging.getLogger()


@pytest.fixture(scope='module')
def open_login_page(user_login_fixture):
    user_login_fixture \
        .click_main_login_button() \
        .verify_page_is_opened()


def test_user_login(request, user_login_fixture, popup_fixture, home_fixture):
    logger.info('\nRunning %s', request.node.name)

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
                             (get_random_string(), PASSWORD, ErrorMessages.INVALID_EMAIL_FORMAT),
                             ('', '', ''),
                             (EMAIL, '', ''),
                             ('', PASSWORD, '')
                         ],
                         ids=[
                             'Correct email, incorrect password',
                             'Incorrect email, correct password',
                             'Random string as email, correct password',
                             'Empty email, empty password',
                             'Correct email, empty password',
                             'Empty email, correct password'
                         ]
                         )
def test_user_login_negative(request, user_login_fixture, open_login_page, email, password, error):
    logger.info('\nRunning %s', request.node.name)

    user_login_fixture \
        .input_email(email) \
        .input_password(password) \
        .click_login_button()

    if error:
        user_login_fixture \
            .verify_notification_error_text(error.value)

    user_login_fixture \
        .verify_page_is_opened()
