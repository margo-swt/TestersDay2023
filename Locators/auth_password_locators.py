from appium.webdriver.common.appiumby import AppiumBy
from common import CommonFeatures as CF

CONFIRM_PROVIDED_EMAIL = (AppiumBy.ID, "com.booking:id/identity_header_description")

BUTTON_ENTER_PASSWORD = (AppiumBy.ID,
                         "com.booking:id/identity_text_input_edit_text")

BUTTON_SIGNIN = (AppiumBy.XPATH,
                 "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                 "/android.view.ViewGroup/android.widget.FrameLayout["
                 "2]/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android"
                 ".widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.widget.Button")


class FindAuthenticationPwdLocators(CF):

    def __init__(self):
        pass

    def find_provided_email(self):
        provided_email_data = CF.find_element_to_be_visible(self, CONFIRM_PROVIDED_EMAIL)
        return provided_email_data

    def find_password_input_field(self):
        password_input_field = CF.find_element_to_be_visible(self, BUTTON_ENTER_PASSWORD)
        return password_input_field

    def find_signin_button(self):
        signin_button = CF.find_element_to_be_visible(self, BUTTON_SIGNIN)
        return signin_button
