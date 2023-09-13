from appium.webdriver.common.appiumby import AppiumBy
from common import CommonFeatures as CF

BUTTON_CONT_WITH_EMAIL = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                          ".widget"
                                          ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout["
                                          "2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                          ".LinearLayout/android.widget.LinearLayout/android.widget.ScrollView/android"
                                          ".widget.LinearLayout/android.widget.FrameLayout["
                                          "1]/android.widget.FrameLayout/android.widget.Button")

SIGN_IN_OR_CREATE_ACCOUNT = (AppiumBy.ID, "com.booking:id/identity_header_title")
X_BUTTON = (AppiumBy.XPATH, "//android.widget.ImageButton[@content-desc='Navigate up']")
TOUCH_OUTSIDE = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                 ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget"
                                 ".FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
                                 ".LinearLayout/android.view.ViewGroup/androidx.viewpager.widget.ViewPager/androidx"
                                 ".recyclerview.widget.RecyclerView/androidx.compose.ui.platform.ComposeView/android"
                                 ".view.View/android.view.View[2]")


class FindIntoPageLocatorContinueWithEmail(CF):

    def __init__(self):
        pass

    def find_page_title(self):
        title_sign_in_or_create_account = CF.find_element_to_be_visible(self, SIGN_IN_OR_CREATE_ACCOUNT)
        return title_sign_in_or_create_account

    def find_intro_page_locator_continue_with_email(self):
        intro_page_locator_continue_with_email = CF.find_element_to_be_visible(self, BUTTON_CONT_WITH_EMAIL)
        return intro_page_locator_continue_with_email

    def find_intro_page_locator_x(self):
        intro_page_locator_x = CF.find_element_to_be_visible(self, X_BUTTON)
        return intro_page_locator_x

    def find_intro_page_locator_touch_outside_modal(self):
        intro_page_locator_touch_outside_modal = CF.find_element_to_be_clickable(self, TOUCH_OUTSIDE)
        return intro_page_locator_touch_outside_modal
