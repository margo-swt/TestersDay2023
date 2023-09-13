from pytest_assume.plugin import assume

from Locators.search_result_locators import FindSearchResultPageLocators

find_search_results_locators = FindSearchResultPageLocators()


def click_sort_button():
    with assume: assert find_search_results_locators.find_sort_button().is_displayed()
    find_search_results_locators.find_sort_button().click()


def click_filter_button():
    with assume: assert find_search_results_locators.find_filter_button().is_displayed()
    find_search_results_locators.find_filter_button().click()


def click_first_wishlist_icon():
    with assume: assert find_search_results_locators.find_first_wishlist_icon().is_displayed()
    find_search_results_locators.find_first_wishlist_icon().click()


def click_second_wishlist_icon():
    with assume: assert find_search_results_locators.find_second_wishlist_icon().is_displayed()
    find_search_results_locators.find_second_wishlist_icon().click()


def assert_alert_added_to_wishlist():
    actual_result = find_search_results_locators.find_saved_hotel_alert()
    expected_substring = "Saved to"
    with assume: assert expected_substring in actual_result, f"Expected '{expected_substring}' to be in '{actual_result}'"


def click_chosen_first_hotel():
    with assume: assert find_search_results_locators.find_and_choose_first_hotel().is_displayed()
    find_search_results_locators.find_and_choose_first_hotel().click()
