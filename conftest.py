import pytest
import allure
from src.modules.wrapper.api_requests_wrapper import post_request
from src.endpoints.api_constants import APIConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import payload_create_booking,payload_create_token
from src.modules.verification.common_verification import *
import logging


@pytest.fixture
def setup():
    print("Setup is started")
    yield
    print("Ending the test case")

    # all the common code which I want to execute here


#@pytest.fixture
#def db_connected():
#    print("Connect Db")
#   yield "DB"
 #   print("Disconnect DB") '''


# @pytest.fixture
# def browser():
#    driver =launch_browser()
#    yield driver
#     driver.quit()


# create_token()
# booking_id()

@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=APIConstants().url_create_token(),
        auth=None,
        headers=Utils().common_headers_json(),
        payload=payload_create_token(),
        in_json=False
    )

    verify_status_code(response_data_status=response.status_code, expected_data=200)
    verify_json_key_for_not_null_token(response.json()["token"])
    return response.json()["token"]

@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(
        url=APIConstants().url_create_booking(),
        auth=None,
        headers=Utils().common_headers_json(),
        payload=payload_create_booking(),
        in_json=False
    )
    booking_id = response.json()["bookingid"]
    verify_status_code(response_data_status=response.status_code, expected_data=200)
    verify_json_key_not_null(booking_id)
    return booking_id