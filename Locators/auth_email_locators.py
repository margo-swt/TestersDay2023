from appium.webdriver.common.appiumby import AppiumBy
from common import CommonFeatures as CF

""""
Do you have design? requirements? do you understand page logics and use cases ? than start creating templates !!!
Variable names = based on element
AppiumBy - to interact with elements on mobile
"""

BUTTON_ENTER_EMAIL = (AppiumBy.XPATH,
                      "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                      "/android.view.ViewGroup/android.widget.FrameLayout["
                      "2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx"
                      ".compose.ui.platform.ComposeView/android.view.View/android.widget.ScrollView/android.view"
                      ".View[2]/android.widget.EditText")

BUTTON_CONTINUE = (AppiumBy.XPATH,
                   "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                   "/android.view.ViewGroup/android.widget.FrameLayout["
                   "2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx"
                   ".compose.ui.platform.ComposeView/android.view.View/android.widget.ScrollView/android.view.View["
                   "3]/android.widget.Button")


class FindAuthenticationLocators(CF):

    def __init__(self):
        pass

    """ find your elements and return them here"""

    def find_email_input_field(self):
        email_input_field = CF.find_element_to_be_visible(self, BUTTON_ENTER_EMAIL)
        return email_input_field

    def find_continue_button(self):
        continue_button = CF.find_element_to_be_visible(self, BUTTON_CONTINUE)
        return continue_button
