from pytest_assume.plugin import assume

from Locators.auth_password_locators import FindAuthenticationPwdLocators

find_password_page_locator = FindAuthenticationPwdLocators()


def input_password():
    with assume: assert find_password_page_locator.find_password_input_field().is_displayed()
    find_password_page_locator.find_password_input_field().click()
    find_password_page_locator.find_password_input_field().send_keys('Paroli12345!')


def click_signin_button():
    with assume: assert find_password_page_locator.find_signin_button().is_displayed()
    find_password_page_locator.find_signin_button().click()
