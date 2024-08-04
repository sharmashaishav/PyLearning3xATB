# Integration Scenarios
# 6. Trying to Update on a Delete Id -> 404

import pytest
import allure
import requests


@allure.title("TC-05 Creating Invalid Booking")
@allure.description("# 5. Invalid Creation - enter a wrong payload or Wrong JSON.")
@allure.label("TC#5")

def test_Invalid_Booking(create_booking):
    url = "https://restful-booker.herokuapp.com/booking/"
    headers = {
        "Content-Type": "application/json"
    }
    payload ={ }

    response = requests.post(url=url,headers=headers,json=payload)
    assert response.status_code == 500
    print(response)
