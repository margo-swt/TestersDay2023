from pytest_assume.plugin import assume

from Locators.filter_modal_locators import FindFilterModalLocators

find_filter_modal_locators = FindFilterModalLocators()


def click_filter_button():
    filter_button = find_filter_modal_locators.find_filter_button()
    with assume: assert filter_button.is_displyed()
    filter_button.click()


def assert_filter_modal_title():
    actual_result = find_filter_modal_locators.find_filter_modal_title()
    expected_substring = "Set your filters"
    with assume: assert expected_substring in actual_result, f"Expected '{expected_substring}' to be in '{actual_result}'"


def choose_price_range_start():
    price_range_start = find_filter_modal_locators.find_filter_modal_price_range_start()
    with assume: assert price_range_start.is_displayed()
    price_range_start.click()


def choose_price_range_end():
    price_range_end = find_filter_modal_locators.find_filter_modal_price_range_end()
    with assume: assert price_range_end.is_displayed()
    price_range_end.click()


def assert_travel_sustainable_properties_title_and_click_toggle():
    actual_result = find_filter_modal_locators.find_travel_sustainable_properties_title()
    expected_substring = "Travel Sustainable properties"
    toggle_button = find_filter_modal_locators.find_travel_sustainable_properties_toggle()
    with assume: assert expected_substring in actual_result, f"Expected '{expected_substring}' to be in '{actual_result}'"
    # if actual_result.is_displayed():
    toggle_button.click()


def assert_property_rating_title_and_click_three_stars():
    actual_result = find_filter_modal_locators.find_property_rating_title()
    expected_substring = "Property rating"
    option_button = find_filter_modal_locators.find_property_rating_three_stars()
    with assume: assert expected_substring in actual_result, f"Expected '{expected_substring}' to be in '{actual_result}'"
    if actual_result.is_displayed():
        option_button.click()


def assert_free_cancellation_title_and_click_toggle():
    actual_result = find_filter_modal_locators.find_free_cancellation_title()
    expected_substring = "Free cancellation"
    toggle_button = find_filter_modal_locators.find_free_cancellation_toggle()
    with assume: assert expected_substring in actual_result, f"Expected '{expected_substring}' to be in '{actual_result}'"
    if actual_result.is_displayed():
        toggle_button.click()


def assert_beds_section_quantity():
    actual_result_find_beds_title = find_filter_modal_locators.find_beds_title()
    expected_substring_beds_title = "Beds"

    actual_result_find_number_of_beds_title = find_filter_modal_locators.find_number_of_beds_title()
    expected_substring_number_of_beds_title = "Number of beds"

    increase_button = find_filter_modal_locators.find_number_of_beds_increase()
    with assume: assert expected_substring_beds_title in actual_result_find_beds_title, f"Expected '{expected_substring_beds_title}' to be in '{actual_result_find_beds_title}'"
    with assume: assert expected_substring_number_of_beds_title in actual_result_find_number_of_beds_title, f"Expected '{expected_substring_number_of_beds_title}' to be in '{actual_result_find_number_of_beds_title}'"

    if actual_result_find_beds_title.is_displayed() and actual_result_find_number_of_beds_title.is_displayed():
        increase_button.click()


def click_show_result_button():
    show_result_button = find_filter_modal_locators.find_show_result_button()
    with assume: assert show_result_button.is_displayed()
    show_result_button.click()
