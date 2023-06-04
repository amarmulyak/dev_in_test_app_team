from framework.locators import LoginPageLocators
from framework.page_objects.page import Page


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_page_locators = LoginPageLocators()

    def click_main_login_button(self):
        self.click_element(self.login_page_locators.main_login_button)
        return self

    def click_login_button(self):
        self.click_element(self.login_page_locators.login_button)
        return self

    def input_email(self, email: str):
        self.send_keys(self.login_page_locators.email_field, email)
        return self

    def input_password(self, password: str):
        self.send_keys(self.login_page_locators.password_field, password)
        return self
