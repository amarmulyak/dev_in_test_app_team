import logging

from framework.locators import LoginPageLocators, NotificationLocators
from framework.page_objects.page import Page

logger = logging.getLogger()


class LoginPage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.login_page_locators = LoginPageLocators()
        self.notification_locators = NotificationLocators()

    def click_main_login_button(self):
        logger.info('Click "Log In" button on the Welcome page')

        self.click_element(self.login_page_locators.main_login_button)
        return self

    def click_login_button(self):
        logger.info('Click "Log In" button')

        self.click_element(self.login_page_locators.login_button)
        return self

    def input_email(self, email: str):
        logger.info('Input "%s"into "Email" field', email)

        self.send_keys(self.login_page_locators.email_field, email)
        return self

    def input_password(self, password: str):
        logger.info('Input "%s" into "Password" field', password)

        self.send_keys(self.login_page_locators.password_field, password)
        return self

    def get_notification_error_text(self):
        logger.info('Get error text from Notification pop up')

        return self.get_element_text(self.notification_locators.error_message_locator)

    def verify_page_is_opened(self):
        logger.info('Verify Log In page is opened')

        login_button = self.find_element(self.login_page_locators.login_button)
        assert login_button.is_displayed(), logger.error('Log In page is not opened')

    def verify_notification_error_text(self, expected_text: str):
        logger.info('Verify Notification pop up error has "%s" text', expected_text)

        actual_text = self.get_notification_error_text()
        assert actual_text == expected_text, logger.error('Actual: "%s", Expected: "%s"', actual_text, expected_text)
