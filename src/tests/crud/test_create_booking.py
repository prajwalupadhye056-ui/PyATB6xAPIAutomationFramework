import pytest
import allure
from src.modules.wrapper.api_requests_wrapper import post_request
from src.endpoints.api_constants import APIConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import payload_create_booking
from src.modules.verification.common_verification import *
import logging



class TestCreateBooking:

    @pytest.mark.positive
    @allure.title("Verify that Creating Booking status and Booking ID shouldn't be null")
    @allure.description(
        "Creating a booking from the payload and verify that booking id should not be null and status code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        logs =logging.getLogger(__name__)
        logs.info("Starting the test.........")
        logs.info("POST Req. started.")

        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )

        logs.info("POST Req. Done")
        logs.info("Now Verify")
        verify_status_code(response_data_status=response.status_code, expected_data=200)
        verify_json_key_not_null(response.json()["bookingid"])

    def test_create_booking_negative_tc1(self):
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json=False
        )

        verify_status_code(response_data_status=response.status_code, expected_data=500)


    def test_create_booking_negative_tc2(self):
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload={"firstname":"prajwal"},
            in_json=False
        )

        verify_status_code(response_data_status=response.status_code, expected_data=500)


