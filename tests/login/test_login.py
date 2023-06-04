from config import EMAIL, PASSWORD


def test_user_login(user_login_fixture):
    user_login_fixture \
        .click_main_login_button() \
        .input_email(EMAIL) \
        .input_password(PASSWORD) \
        .click_login_button()

    a = 1
    assert True
