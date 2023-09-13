from appium.webdriver.common.appiumby import AppiumBy
from common import CommonFeatures as CF


WISHLIST_ICON_FIRST = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                       ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                       "/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
                                       ".LinearLayout/androidx.compose.ui.platform.ComposeView/android.view.View"
                                       "/android.view.View/android.view.ViewGroup/android.widget.FrameLayout/androidx"
                                       ".compose.ui.platform.ComposeView/android.view.View/android.view.ViewGroup"
                                       "/android.widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android"
                                       ".view.View/android.view.ViewGroup/android.widget.FrameLayout/androidx.compose"
                                       ".ui.platform.ComposeView/android.view.View/android.view.View/android.view"
                                       ".View[1]/android.view.View[3]")
WISHLIST_ICON_SECOND = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                        ".widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout"
                                        "/android.view.ViewGroup/android.widget.FrameLayout/android.widget"
                                        ".LinearLayout/androidx.compose.ui.platform.ComposeView/android.view.View"
                                        "/android.view.View/android.view.ViewGroup/android.widget.FrameLayout"
                                        "/androidx.compose.ui.platform.ComposeView/android.view.View/android.view"
                                        ".ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform"
                                        ".ComposeView/android.view.View/android.view.ViewGroup/android.widget"
                                        ".FrameLayout/androidx.compose.ui.platform.ComposeView/android.view.View"
                                        "/android.view.View/android.view.View[2]/android.view.View[3]")
SORT_BUTTON = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                               ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view"
                               ".ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout["
                               "2]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[1]")
FILTER_BUTTON = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                 ".FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view"
                                 ".ViewGroup/android.widget.LinearLayout/android.widget.FrameLayout["
                                 "2]/androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View[2]")
ALERT_SAVED_TO_MY_NEXT_TRIP = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView[1]")

FILTERED_CHOOSE_FIRST_HOTEL = (AppiumBy.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                               "/android.widget.FrameLayout/android.widget.LinearLayout/android"
                                               ".widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout"
                                               "/android.widget.LinearLayout/androidx.compose.ui.platform.ComposeView"
                                               "/android.view.View/android.view.View/android.view.ViewGroup/android"
                                               ".widget.FrameLayout/androidx.compose.ui.platform.ComposeView/android"
                                               ".view.View/android.view.ViewGroup/android.widget.FrameLayout/androidx"
                                               ".compose.ui.platform.ComposeView/android.view.View/android.view"
                                               ".ViewGroup/android.widget.FrameLayout/androidx.compose.ui.platform"
                                               ".ComposeView/android.view.View/android.view.View/android.view.View[1]")


class FindSearchResultPageLocators(CF):

    def __init__(self):
        pass

    def find_first_wishlist_icon(self):
        first_wishlist_icon = CF.find_element_to_be_visible(self, WISHLIST_ICON_FIRST)
        return first_wishlist_icon

    def find_second_wishlist_icon(self):
        second_wishlist_icon = CF.find_element_to_be_visible(self, WISHLIST_ICON_SECOND)
        return second_wishlist_icon

    def find_sort_button(self):
        sort_button = CF.find_element_to_be_visible(self, SORT_BUTTON)
        return sort_button

    def find_filter_button(self):
        filter_button = CF.find_element_to_be_visible(self, FILTER_BUTTON)
        return filter_button

    def find_saved_hotel_alert(self):
        alert_info = CF.find_element_to_be_visible(self, ALERT_SAVED_TO_MY_NEXT_TRIP)
        return alert_info.text

    def find_and_choose_first_hotel(self):
        find_choose_hotel = CF.find_element_to_be_clickable(self, FILTERED_CHOOSE_FIRST_HOTEL)
        return find_choose_hotel
