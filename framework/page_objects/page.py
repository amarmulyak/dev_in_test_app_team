from appium.webdriver.common.appiumby import AppiumBy
from utils.utils import retry


class Page:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator: tuple[AppiumBy, str]):
        return self.driver.find_element(*locator)

    @retry()
    def click_element(self, locator: tuple[AppiumBy, str]):
        self.find_element(locator).click()

    def send_keys(self, locator: tuple[AppiumBy, str], text: str):
        self.find_element(locator).send_keys(text)
