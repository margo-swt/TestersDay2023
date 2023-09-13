from appium.webdriver.common.appiumby import AppiumBy
from common import CommonFeatures as CF


FILTER_BUTTON = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]")
SET_YOUR_FILTERS_TITLE = (AppiumBy.XPATH,
                          "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.LinearLayout[1]/android.widget.TextView")
# RESET_FILTER_BUTTON =
# NIGHT_COUNT = (AppiumBy.ID, "")
FILTER_PRICE_START = (AppiumBy.XPATH, "//android.widget.SeekBar[@content-desc='Range start,US$500']")
FILTER_PRICE_END = (AppiumBy.XPATH, "//android.widget.SeekBar[@content-desc='Range end,US$1500']")
# POPULAR_FILTERS_TITLE = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView")
TRAVEL_SUSTAINABLE_PROPS_TITLE = (AppiumBy.XPATH,
                                  "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.TextView")
TRAVEL_SUSTAINABLE_PROPS_TOGGLE = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.Switch")

PROPERTY_RATING_TITLE = (AppiumBy.XPATH,
                         "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[3]/android.view.ViewGroup/android.widget.TextView")
PROPERTY_RATING_THREE_STARS = (AppiumBy.XPATH,
                               "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[1]/android.widget.FrameLayout[4]/android.widget.LinearLayout/android.widget.TextView")

PROPERTY_TYPE_TITLE = (AppiumBy.XPATH,
                       "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.view.ViewGroup/android.widget.TextView")
PROPERTY_TYPE_HOTELS = (AppiumBy.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.view.ViewGroup[2]/android.widget.FrameLayout[4]/android.widget.LinearLayout/android.widget.TextView")

FREE_CANCELLATION_TITLE = (AppiumBy.XPATH,
                           "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.TextView")
FREE_CANCELLATION_TOGGLE = (AppiumBy.ID, "com.booking:id/switch_widget")

BEDS_TITLE = (AppiumBy.XPATH,
              "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.widget.TextView")
NUMBER_OF_BEDS_TITLE = (AppiumBy.XPATH,
                        "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView")
NUMBER_OF_BEDS_INCREASE = (AppiumBy.XPATH, "//android.widget.Button[@content-desc='Increase']")

SHOW_RESULT_BUTTON = (AppiumBy.ID, "com.booking:id/apply_button")


class FindFilterModalLocators(CF):

    def __init__(self):
        pass

    def find_filter_button(self):
        filter_btn = CF.find_element_to_be_clickable(self, FILTER_BUTTON)
        return filter_btn

    def find_filter_modal_title(self):
        filter_modal_title = CF.find_element_to_be_visible(self, SET_YOUR_FILTERS_TITLE)
        return filter_modal_title.text

    def find_filter_modal_price_range_start(self):
        price_range_start = CF.find_element_to_be_visible(self, FILTER_PRICE_START)
        return price_range_start

    def find_filter_modal_price_range_end(self):
        price_range_end = CF.find_element_to_be_visible(self, FILTER_PRICE_END)
        return price_range_end

    def find_travel_sustainable_properties_title(self):
        travel_sustainable_properties_title = CF.find_element_to_be_visible(self, TRAVEL_SUSTAINABLE_PROPS_TITLE)
        return travel_sustainable_properties_title.text

    def find_travel_sustainable_properties_toggle(self):
        travel_sustainable_properties_toggle = CF.find_element_to_be_visible(self, TRAVEL_SUSTAINABLE_PROPS_TOGGLE)
        return travel_sustainable_properties_toggle.text

    def find_free_cancellation_title(self):
        free_cancellation_title = CF.find_element_to_be_visible(self, FREE_CANCELLATION_TITLE)
        return free_cancellation_title.text

    def find_free_cancellation_toggle(self):
        free_cancellation_toggle = CF.find_element_to_be_visible(self, FREE_CANCELLATION_TOGGLE)
        return free_cancellation_toggle.text

    def find_property_rating_title(self):
        property_rating_title = CF.find_element_to_be_visible(self, PROPERTY_RATING_TITLE)
        return property_rating_title.text

    def find_property_rating_three_stars(self):
        property_rating_three_stars = CF.find_element_to_be_visible(self, PROPERTY_RATING_THREE_STARS)
        return property_rating_three_stars

    def find_beds_title(self):
        beds_title = CF.find_element_to_be_visible(self, BEDS_TITLE)
        return beds_title.text

    def find_number_of_beds_title(self):
        number_of_beds_title = CF.find_element_to_be_visible(self, NUMBER_OF_BEDS_TITLE)
        return number_of_beds_title.text

    def find_number_of_beds_increase(self):
        number_of_beds_increase = CF.find_element_to_be_visible(self, NUMBER_OF_BEDS_INCREASE)
        return number_of_beds_increase

    def find_show_result_button(self):
        show_result_button = CF.find_element_to_be_visible(self, SHOW_RESULT_BUTTON)
        return show_result_button
