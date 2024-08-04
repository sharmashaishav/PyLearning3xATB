# Integration Scenarios

import pytest
import allure
import requests


@allure.title("TC-06 # 6. Trying to Update on a Delete Id -> 404")
@allure.description("# 6. Invalid Update - # 6. Trying to Update on a Delete Id")
@allure.label("TC#6")
def test_UPDATE_DELETED_BOOKING(create_booking,create_token):
    URL = "https://restful-booker.herokuapp.com/booking/"
    DELETE_URL = URL + str(create_booking)
    cookie_value = "token=" + create_token
    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie_value
    }
    response = requests.get(url=DELETE_URL, headers=headers)
    print("\nBooking ID to be DELETED is --> ",create_booking)
    response = requests.delete(url=DELETE_URL, headers=headers)
    assert response.status_code == 201
    print(f"Booking ID {create_booking} DELETED successfully")
    payload = {
        "firstname": "Shaishav",
        "lastname": "Sharma",
        "totalprice": 8000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-03"
        },
        "additionalneeds": "Breakfast"
    }
    updateResponse = requests.put(url= DELETE_URL,headers=headers,json=payload)
    assert updateResponse.status_code in [404, 405]
    print("\nDeleted ID CANNOT be UPDATED")
    getresposnse = requests.get(url=DELETE_URL,headers=headers)
    assert updateResponse.status_code in [404, 405]
    print("\nDeleted ID CANNOT be FETCHED")
