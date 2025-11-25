import pytest
import allure
from pydantic import ValidationError
from core.models.booking import BookingResponse
from requests.exceptions import HTTPError


@allure.feature('Test creating booking')
@allure.story('Positive: creating booking with custom data')
def test_create_booking_with_custom_data(api_client):
    booking_data = {
        "firstname": "Ivan",
        "lastname": "Ivanovich",
        "totalprice": 150,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-18"
        },
        "additionalneeds": "Dinner"
    }

    response = api_client.create_booking(booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation failed: {e}")

    assert response['booking']['firstname'] == booking_data['firstname']
    assert response['booking']['lastname'] == booking_data['lastname']
    assert response['booking']['totalprice'] == booking_data['totalprice']
    assert response['booking']['depositpaid'] == booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == booking_data['additionalneeds']


@allure.feature('Test creating booking')
@allure.story('Positive: creating booking with random data')
def test_create_booking_with_random_data(api_client, generate_random_booking_data):

    response = api_client.create_booking(generate_random_booking_data)
    try:
        BookingResponse(**response)
    except ValidationError as e:
        raise ValidationError(f"Response validation failed: {e}")

    assert response['booking']['firstname'] == generate_random_booking_data['firstname']
    assert response['booking']['lastname'] == generate_random_booking_data['lastname']
    assert response['booking']['totalprice'] == generate_random_booking_data['totalprice']
    assert response['booking']['depositpaid'] == generate_random_booking_data['depositpaid']
    assert response['booking']['bookingdates']['checkin'] == generate_random_booking_data['bookingdates']['checkin']
    assert response['booking']['bookingdates']['checkout'] == generate_random_booking_data['bookingdates']['checkout']
    assert response['booking']['additionalneeds'] == generate_random_booking_data['additionalneeds']


@allure.feature('Test creating booking')
@allure.story('Negative: creating booking with invalid data')
def test_create_booking_with_invalid_data(api_client):
    invalid_booking_data = {
        "firstname": 150,
        "lastname": 150,
        "totalprice": "Ivanovich",
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2025-02-01",
            "checkout": "2025-02-18"
        },
        "additionalneeds": "Dinner"
    }

    with pytest.raises(HTTPError):
        api_client.create_booking(invalid_booking_data)






