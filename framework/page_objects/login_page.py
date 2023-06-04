from framework.locators import LoginLocators
from framework.page_objects.page import Page


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_locators = LoginLocators()

    def click_main_login_button(self):
        self.click_element(self.login_locators.main_login_button)
        return self

    def click_login_button(self):
        self.click_element(self.login_locators.login_button)
        return self

    def input_email(self, email: str):
        self.send_keys(self.login_locators.email_field, email)
        return self

    def input_password(self, password: str):
        self.send_keys(self.login_locators.password_field, password)
        return self
