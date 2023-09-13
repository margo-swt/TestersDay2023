from pytest_assume.plugin import assume

from Locators.sort_modal_locators import FindSortModalLocators

find_sort_modal_locators = FindSortModalLocators()


def assert_sort_modal_title():
    actual_result = find_sort_modal_locators.find_sort_modal_title()
    expected_substring = "Sort by"
    with assume: assert expected_substring in actual_result, f"Expected '{expected_substring}' to be in '{actual_result}'"


def choose_sort_by_price_low_to_high():
    sort_modal_price_low_to_high = find_sort_modal_locators.find_sort_modal_price_low_to_high()
    with assume: assert sort_modal_price_low_to_high.is_displayed()
    sort_modal_price_low_to_high.click()


def assert_red_dot_visibility_on_sort_button():
    sort_section_red_dot = find_sort_modal_locators.find_sort_section_red_dot()
    with assume: assert sort_section_red_dot.is_displayed()
