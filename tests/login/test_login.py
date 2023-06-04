from config import EMAIL, PASSWORD


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
