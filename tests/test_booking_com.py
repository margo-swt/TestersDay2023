import time

from PageActions.auth_email_actions import *
from PageActions.auth_password_actions import *
from PageActions.filter_modal_actions import *
from PageActions.intro_page_actions import *
from PageActions.search_actions import *
from PageActions.search_results_actions import *
from PageActions.sort_modal_actions import *


class TestBookHotel:
    def test_book_hotel(self):

        """intro page - authorisation of existing user"""
        verify_visibility_of_title_on_intro_page()
        click_intro_redirection_email_button()
        input_email_value()
        click_continue_button()
        input_password()
        click_signin_button()
        click_x_on_intro_page()
        click_outside_intro_page()
        click_x_on_intro_page()
        input_search_hotel_destination_name()

        """guest request of search params"""
        click_search_destination_results()
        click_calendar_range_start_date()
        click_calendar_range_end_date()
        click_calendar_range_submit()
        click_guest_request_field()
        click_guest_request_room_increase()
        click_guest_request_room_decrease()
        click_guest_request_adults_increase()
        click_guest_request_adults_decrease()
        click_guest_request_apply()
        click_guest_request_apply_submit_search()

        """click_sort_button() - opens sort modal"""
        click_sort_button()
        assert_sort_modal_title()
        choose_sort_by_price_low_to_high()
        assert_red_dot_visibility_on_sort_button()

        """filter sorted data"""
        time.sleep(5)
        click_filter_button()
        assert_filter_modal_title()
        # choose_price_range_start()
        # choose_price_range_end()
        #toggle button issues
        assert_travel_sustainable_properties_title_and_click_toggle()
        assert_property_rating_title_and_click_three_stars()
        assert_free_cancellation_title_and_click_toggle()
        assert_beds_section_quantity()
        click_show_result_button()

        """choosing hotel properties"""
        click_first_wishlist_icon()
        assert_alert_added_to_wishlist()
        click_second_wishlist_icon()
        assert_alert_added_to_wishlist()
        click_chosen_first_hotel()

        assert """your scenario based expected result assertion should go by the end of each test"""



