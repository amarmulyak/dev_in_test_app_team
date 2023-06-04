from appium.webdriver.common.appiumby import AppiumBy


class HomePageLocators:
    def __init__(self):
        self.side_bar_menu_button = AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.LinearLayout[2]/android.view.ViewGroup/android.widget.FrameLayout/android.widget.ImageView'

