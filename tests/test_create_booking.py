import allure
import pytest
import requests


@allure.feature('Test Create Booking')
@allure.story('Test successful booking creation')
def test_create_booking_success(api_client, sample_booking_data):
    booking_id = api_client.create_booking(sample_booking_data)
    assert isinstance(booking_id, int), f"Expected booking_id to be int but got {type(booking_id)}"