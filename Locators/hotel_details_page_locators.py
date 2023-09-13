from appium.webdriver.common.appiumby import AppiumBy
from common import CommonFeatures as CF

"""Template example"""

HOTEL_NAME =
SELECT_ROOMS_BTN =
PRICE_ROOM_CARD =

CHOOSE_YOUR_STAY_TITLE =
TWIN_ROOM_CONTAINS =
SELECT_ROOM_BTN =
RESERVE_BTN =
CHOSEN_ROOM_PRICE =


# #NEW MODULE
# FILL_IN_YOUR_INFO_TITLE =
# FIRST_NAME_REQ =
# LAST_NAME_REQ =
# EMAIL_ADDRESS_REQ =
# COUNTRY_REQ =
# MOBILE_REQ =
# PURPOSE_TITLE =
# LEISURE_TITLE =
# LT_RADIO_BTN =
# BUSINESS_TITLE =
# BT_RADIO_BTN =
# NEXT_STEP_BTN =

# #NEW MODULE
# BOOKING_OVERVIEW_TITLE =
# BO_HOTEL_NAME =
# CHECK_IN_DATE =
# CHECK_OUT_DATE =
# GUEST_REQUESTS =
# TOTAL_TITLE =
# TOTAL_PRICE =
# FINAL_STEP_BTN =

# #NEW
# FINISH_BOOKING_TITLE =
# WHEN_DO_U_WANT_TO_PAY =
# PAY_AT_THE_PROP =
# PAY_NOW =
# SUM_PRICE =
# TOTAL_PRICE =
# HOTEL_NAME =
# CHECK_IN_DATE =
# CHECK_OUT_DATE =
# GUEST_REQUESTS =
# MAIL =

class FindHotelDetailsPage(CF):

    def __init__(self):
        pass

    def find_hotel_detail_page(self):
        hotel_detail_page = CF.find_element_to_be_visible(self, HOTEL_NAME)
        return hotel_detail_page



