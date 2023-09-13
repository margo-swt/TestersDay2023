from appium.webdriver.common.touch_action import TouchAction
from pytest_assume.plugin import assume
from conftest import my_driver
from Locators.intro_page_locators import FindIntoPageLocatorContinueWithEmail

find_intro_locators = FindIntoPageLocatorContinueWithEmail()
# driver = RemoteDriverCaps()


def click_intro_redirection_email_button():
    with assume: assert find_intro_locators.find_intro_page_locator_continue_with_email().is_displayed()
    find_intro_locators.find_intro_page_locator_continue_with_email().click()


def verify_visibility_of_title_on_intro_page():
    with assume: assert find_intro_locators.find_page_title().is_displayed()
    find_intro_locators.find_page_title()


def click_x_on_intro_page():
    with assume: assert find_intro_locators.find_intro_page_locator_x().is_displayed()
    find_intro_locators.find_intro_page_locator_x().click()


def click_outside_intro_page():
    outside_intro_page = find_intro_locators.find_intro_page_locator_touch_outside_modal()
    with assume: assert outside_intro_page.is_displayed()
    outside_intro_page.click()

