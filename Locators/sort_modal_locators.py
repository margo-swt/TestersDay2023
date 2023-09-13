from appium.webdriver.common.appiumby import AppiumBy
from common import CommonFeatures as CF


SORT_BY_TITLE = (AppiumBy.ID, "com.booking:id/facet_with_bottom_sheet_header_title")
ENTIRE_HOMES_AND_APTS_FIRST = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.CheckedTextView[1]")
DISTANCE_FROM_DOWNTOWN = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.CheckedTextView[2]")
POPULARITY = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.CheckedTextView[3]")
PROPERTY_RATING_HTL = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.CheckedTextView[4]")
PROPERTY_RATING_LTH = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.CheckedTextView[5]")
GUEST_REVIEW_SCORE = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.CheckedTextView[6]")
PRICE_LTH = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.CheckedTextView[6]")
AFTER_SORT_VALUE_RED_DOT = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout[2]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]/android.widget.TextView[1]")


class FindSortModalLocators(CF):

    def __init__(self):
        pass

    def find_sort_modal_title(self):
        sort_modal_title = CF.find_element_to_be_visible(self, SORT_BY_TITLE)
        return sort_modal_title.text

    def find_sort_modal_price_low_to_high(self):
        price_low_to_high = CF.find_element_to_be_visible(self, PRICE_LTH)
        return price_low_to_high

    def find_sort_section_red_dot(self):
        red_dot = CF.find_element_to_be_visible(self, AFTER_SORT_VALUE_RED_DOT)
        return red_dot

    # def find_sort_modal_entire_homes_and_apts(self):
    #     entire_homes_and_apts = CF.find_element_to_be_visible(self, ENTIRE_HOMES_AND_APTS_FIRST)
    #     return entire_homes_and_apts


