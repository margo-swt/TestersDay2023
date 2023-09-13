from appium.webdriver.common.appiumby import AppiumBy
from common import CommonFeatures as CF

DESTINATION_FIELD = (AppiumBy.ACCESSIBILITY_ID, "Enter your destination")

DESTINATION_FIELD_INTERACT = (AppiumBy.ID, "com.booking:id/facet_with_bui_free_search_booking_header_toolbar_content")

SEARCH_RESULT = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                 ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget"
                                 ".LinearLayout/android.widget.FrameLayout/androidx.recyclerview.widget.RecyclerView"
                                 "/android.view.ViewGroup[1]/android.widget.TextView[1]")

CALENDAR_RANGE_START = (AppiumBy.XPATH, "//android.view.View[@content-desc='07 October 2023']")

CALENDAR_RANGE_END = (AppiumBy.XPATH, "//android.view.View[@content-desc='14 October 2023']")

CALENDAR_RANGE_VERIFICATION = (AppiumBy.ID, "com.booking:id/facet_date_picker_selection_summary")

CALENDAR_SELECT_DATES_CONFIRM = (AppiumBy.ID, "com.booking:id/facet_date_picker_confirm")

# DATE_FIELD_COMPARE = (AppiumBy.XPATH, "//android.widget.Button[contains(@content-desc, 'Staying from ')]")

GUEST_REQUEST_FIELD = (AppiumBy.XPATH, "//android.widget.Button[contains(@content-desc, ' room')]")

GRF_ROOM_INCREASE = (AppiumBy.XPATH, "(//android.widget.Button[@content-desc='Increase'])[1]")

GRF_ROOM_DECREASE = (AppiumBy.XPATH, "(//android.widget.Button[@content-desc='Decrease'])[1]")

GRF_ADULTS_INCREASE = (AppiumBy.XPATH, "(//android.widget.Button[@content-desc='Increase'])[2]")

GRF_ADULTS_DECREASE = (AppiumBy.XPATH, "(//android.widget.Button[@content-desc='Decrease'])[2]")

GRF_BUTTON_APPLY = (AppiumBy.ID, "com.booking:id/group_config_apply_button")

BUTTON_SEARCH = (AppiumBy.XPATH, "//android.view.View[@content-desc='Accommodation search "
                                 "box']/android.view.View/android.widget.Button")


class FindSearchParametersLocators(CF):

    def __init__(self):
        pass

    def find_destination_field(self):
        destination_field = CF.find_element_to_be_visible(self, DESTINATION_FIELD)
        return destination_field

    def find_destination_field_modal(self):
        destination_field_modal = CF.find_element_to_be_visible(self, DESTINATION_FIELD_INTERACT)
        return destination_field_modal

    def find_destination_search_result(self):
        destination_field_modal_search_result = CF.find_element_to_be_clickable(self, SEARCH_RESULT)
        return destination_field_modal_search_result

    def find_calendar_range_start(self):
        calendar_modal_start_range = CF.find_element_to_be_visible(self, CALENDAR_RANGE_START)
        return calendar_modal_start_range

    def find_calendar_range_end(self):
        calendar_modal_end_range = CF.find_element_to_be_visible(self, CALENDAR_RANGE_END)
        return calendar_modal_end_range

    def find_calendar_ranges_submit(self):
        calendar_modal_submit_range = CF.find_element_to_be_visible(self, CALENDAR_SELECT_DATES_CONFIRM)
        return calendar_modal_submit_range

    def find_calendar_range_verification(self):
        calendar_modal_range_verification = CF.find_element_to_be_visible(self, CALENDAR_RANGE_VERIFICATION)
        return calendar_modal_range_verification

    def find_guest_request_field(self):
        guest_request = CF.find_element_to_be_visible(self, GUEST_REQUEST_FIELD)
        return guest_request

    def find_guest_request_room_increase(self):
        guest_request_modal_room_increase = CF.find_element_to_be_visible(self, GRF_ROOM_INCREASE)
        return guest_request_modal_room_increase

    def find_guest_request_room_decrease(self):
        guest_request_modal_room_decrease = CF.find_element_to_be_visible(self, GRF_ROOM_DECREASE)
        return guest_request_modal_room_decrease

    def find_guest_request_adults_decrease(self):
        guest_request_modal_adults_decrease = CF.find_element_to_be_visible(self, GRF_ADULTS_DECREASE)
        return guest_request_modal_adults_decrease

    def find_guest_request_adults_increase(self):
        guest_request_modal_adults_increase = CF.find_element_to_be_visible(self, GRF_ADULTS_INCREASE)
        return guest_request_modal_adults_increase

    def find_guest_request_apply(self):
        guest_request_modal_apply = CF.find_element_to_be_visible(self, GRF_BUTTON_APPLY)
        return guest_request_modal_apply

    def find_button_search(self):
        button_search = CF.find_element_to_be_visible(self, BUTTON_SEARCH)
        return button_search
