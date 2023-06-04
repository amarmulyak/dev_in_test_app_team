from .login_locators import LoginLocators
from .page import Page


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_locators = LoginLocators()

    def click_login_button(self):
        self.click_element(self.login_locators.login_button)
        return self

    def input_email(self, email: str):
        self.send_keys(self.login_locators.email_field, email)
        return self
