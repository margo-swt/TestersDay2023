from pytest_assume.plugin import assume

from Locators.auth_email_locators import FindAuthenticationLocators

find_email_locator = FindAuthenticationLocators()

"""NOTE: in page actions you should put basic assertions (checks) for elements, you cant test or assert a scenario 
here, you can use this modules to send keys as well , before you become an advanced QAA and learn data driven approach"""


def input_email_value():
    with assume: assert find_email_locator.find_email_input_field().is_displayed()
    find_email_locator.find_email_input_field().click()
    find_email_locator.find_email_input_field().send_keys("yaneraw525@nickolis.com")


def click_continue_button():
    with assume: assert find_email_locator.find_continue_button().is_displayed()
    find_email_locator.find_continue_button().click()
