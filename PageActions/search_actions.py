from pytest_assume.plugin import assume

from Locators.search_locators import FindSearchParametersLocators

find_search_parameters_locators = FindSearchParametersLocators()


def input_search_hotel_destination_name():
    with assume: assert find_search_parameters_locators.find_destination_field().is_displayed()
    find_search_parameters_locators.find_destination_field().click()
    find_search_parameters_locators.find_destination_field_modal().click()
    find_search_parameters_locators.find_destination_field_modal().send_keys("tokyo")


def click_search_destination_results():
    with assume: assert find_search_parameters_locators.find_destination_search_result().is_displayed()
    find_search_parameters_locators.find_destination_search_result().click()


def click_calendar_range_start_date():
    with assume: assert find_search_parameters_locators.find_calendar_range_start().is_displayed()
    find_search_parameters_locators.find_calendar_range_start().click()


def click_calendar_range_end_date():
    with assume: assert find_search_parameters_locators.find_calendar_range_end().is_displayed()
    find_search_parameters_locators.find_calendar_range_end().click()


def click_calendar_range_submit():
    with assume: assert find_search_parameters_locators.find_calendar_ranges_submit().is_displayed()
    find_search_parameters_locators.find_calendar_ranges_submit().click()


def click_guest_request_field():
    with assume: assert find_search_parameters_locators.find_guest_request_field().is_displayed()
    find_search_parameters_locators.find_guest_request_field().click()


def click_guest_request_room_increase():
    with assume: assert find_search_parameters_locators.find_guest_request_room_increase().is_displayed()
    find_search_parameters_locators.find_guest_request_room_increase().click()


def click_guest_request_room_decrease():
    with assume: assert find_search_parameters_locators.find_guest_request_room_decrease().is_displayed()
    find_search_parameters_locators.find_guest_request_room_decrease().click()


def click_guest_request_adults_increase():
    with assume: assert find_search_parameters_locators.find_guest_request_adults_increase().is_displayed()
    find_search_parameters_locators.find_guest_request_adults_increase().click()


def click_guest_request_adults_decrease():
    with assume: assert find_search_parameters_locators.find_guest_request_adults_decrease().is_displayed()
    find_search_parameters_locators.find_guest_request_adults_decrease().click()


def click_guest_request_apply():
    with assume: assert find_search_parameters_locators.find_guest_request_apply().is_displayed()
    find_search_parameters_locators.find_guest_request_apply().click()


def click_guest_request_apply_submit_search():
    with assume: assert find_search_parameters_locators.find_button_search().is_displayed()
    find_search_parameters_locators.find_button_search().click()
