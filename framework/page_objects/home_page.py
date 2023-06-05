import logging

from framework.locators import HomePageLocators
from framework.page_objects.page import Page

logger = logging.getLogger()


class HomePage(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.home_page_locators = HomePageLocators()

    def verify_page_is_opened(self):
        logger.info('Verify Home page is opened')
        side_bar_menu_button = self.find_element(self.home_page_locators.side_bar_menu_button)
        assert side_bar_menu_button.is_displayed()
