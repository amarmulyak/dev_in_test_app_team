from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

from utils.android_utils import android_get_desired_capabilities


driver = webdriver.Remote('http://localhost:4723/wd/hub', android_get_desired_capabilities())

el = driver.find_element(AppiumBy.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.FrameLayout[1]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.widget.Button')
