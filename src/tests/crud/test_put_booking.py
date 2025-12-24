import pytest
import allure
from src.modules.wrapper.api_requests_wrapper import put_request, post_request
from src.endpoints.api_constants import APIConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import (
    payload_update_booking,
    payload_create_token,
    payload_create_booking
)
from src.modules.verification.common_verification import *


class TestPutBooking:

    @pytest.mark.positive
    @allure.title("Verify that existing booking ID with existing token can be updated using PUT")
    @allure.description("Create a booking, generate token, and update the booking using PUT")
    def test_verify_existing_booking_update_put(self):
        # Step 1: Generate token
        token_response = post_request(
            url=APIConstants().url_create_token(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_token(),
            in_json=False
        )
        token = token_response.json()["token"]

        # Step 2: Create a booking to update
        create_response = post_request(
            url=APIConstants().url_create_booking(),
            auth=None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )
        booking_id = create_response.json()["booking_id"]

        # Step 3: Update the booking using PUT
        response = put_request(
            url=APIConstants().url_patch_put_delete(booking_id),
            headers=Utils().common_header_put_delete_patch_cookie(token),
            payload=payload_update_booking(),
            in_json=False
        )

        # Step 4: Assertions
        verify_status_code(response_data_status=response.status_code, expected_data=200)










