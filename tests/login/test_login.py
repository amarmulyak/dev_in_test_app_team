def test_user_login(user_login_fixture):
    user_login_fixture \
        .click_login_button() \
        .input_email('asd')

    a = 1
    assert True
