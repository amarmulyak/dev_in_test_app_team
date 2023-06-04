from framework.locators import LoginPageLocators, NotificationLocators
from framework.page_objects.page import Page

class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_page_locators = LoginPageLocators()
        self.notification_locators = NotificationLocators()

    def verify_page_is_opened(self):
        login_button = self.find_element(self.login_page_locators.login_button)
        assert login_button.is_displayed()

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

    def get_notification_error_text(self):
        return self.get_element_text(self.notification_locators.error_message_locator)
