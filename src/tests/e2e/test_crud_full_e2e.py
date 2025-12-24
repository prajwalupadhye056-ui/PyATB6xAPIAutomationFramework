
import pytest
import allure
from src.modules.wrapper.api_requests_wrapper import post_request,put_request,delete_request
from src.endpoints.api_constants import APIConstants
from src.utils.utils import Utils
from src.modules.payload_manager.payload_manager import payload_create_booking, payload_update_booking
from src.modules.verification.common_verification import *
import logging



#Flow of the E2E

#Create a token
#Create a booking id
#We need to update booking ID with token
#We are going to delete the booking ID
# We are going to verify that Booking ID does not exist after delete

#conftest

class TestCrudBooking(object):

    @allure.title("Test CRUD operation Update(PUT).")
    @allure.description("Verify that full update with the booking ID and token is working")
    def test_update_booking_id_token(self,create_token,get_booking_id):
        put_url=APIConstants().url_patch_put_delete(booking_id=get_booking_id)
        print(put_url)
        print(create_token)

        response= put_request(

            url=put_url,
            headers=Utils().common_header_put_delete_patch_cookie(token=create_token),
            payload=payload_update_booking(),
            auth=None,
            in_json=False
        )

        #Verify

        verify_status_code(response_data_status=response.status_code, expected_data=200)
        verify_response_key(response.json()["firstname"], expected_data="Amit")
        verify_response_key(response.json()["lastname"],  expected_data="Brown")

    def test_delete_booking_id(self,create_token,get_booking_id):
         delete_url= APIConstants().url_patch_put_delete(booking_id=get_booking_id)
         response = delete_request(

             url=delete_url,
             headers=Utils().common_header_put_delete_patch_cookie(token=create_token),
             auth=None,
             in_json=False
         )
         verify_response_delete(response=response.text)
         verify_status_code(response_data_status=response.status_code, expected_data=201)



