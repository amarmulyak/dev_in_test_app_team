from appium.webdriver.common.appiumby import AppiumBy


class PopupModalLocators:
    def __init__(self):
        self.deny_button = AppiumBy.ID, 'com.android.permissioncontroller:id/permission_deny_button'

