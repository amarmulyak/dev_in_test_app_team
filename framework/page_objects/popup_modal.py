import logging

from framework.locators import PopupModalLocators
from framework.page_objects.page import Page

logger = logging.getLogger()


class PopupModal(Page):
    def __init__(self, driver):
        super().__init__(driver)
        self.popup_modal_locators = PopupModalLocators()

    def click_deny_button(self):
        logger.info('Click "Deny" button on the Pop Up')

        self.click_element(self.popup_modal_locators.deny_button)
        return self
