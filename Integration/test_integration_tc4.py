# Integration Scenarios

# 5. Invalid Creation - enter a wrong payload or Wrong JSON.
# 6. Trying to Update on a Delete Id -> 404

import pytest
import allure
import requests


@allure.title("TC-04 # 4. Create a BOOKING, Delete It")
@allure.description("# 4. Create a BOOKING, Delete It")
@allure.label("TC#4")

def test_CREATE_DELETE_BOOKING(create_booking,create_token):
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