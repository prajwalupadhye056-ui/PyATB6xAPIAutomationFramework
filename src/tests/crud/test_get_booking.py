import pytest
import allure
from src.modules.wrapper.api_requests_wrapper import post_request, get_request
from src.endpoints.api_constants import APIConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import payload_create_booking
from src.modules.verification.common_verification import *
import logging



class TestGetBooking:

    @pytest.mark.positive
    @allure.title("Verify that existing booking which is booking number 1 exists")
    @allure.description("Booking exists")
    def test_verify_existing_booking_bid_01(self):
        booking_id = 1

        response = get_request(
            url=APIConstants().url_patch_put_delete(booking_id),
            auth=None,
            headers = Utils().common_headers_json(),
            in_json = False
             )
        verify_status_code(response_data_status=response.status_code, expected_data=200)
        verify_json_key_not_null(response.json()["firstname"])
        verify_json_key_not_null(response.json()["lastname"])
        verify_json_key_not_null(response.json()["totalprice"])
        verify_json_key_not_null(response.json()["bookingdates"])

    @pytest.mark.negative
    @allure.title("Verify that booking id does not exist")
    @allure.description("Booking does not exist")
    def test_verify_invalid_booking_not_exist(self):
        invalid_booking_id = 999999

        response = get_request(
            url=APIConstants().url_patch_put_delete(invalid_booking_id),
            auth=None,
            headers=Utils().common_headers_json(),
            in_json=False
        )

        verify_status_code(response_data_status=response.status_code, expected_data=404)




    def test_create_booking_negative_tc2(self):
        pass


