# Integration Scenarios

import allure
import pytest
import requests

@allure.title('Integration Scenario-1')
@allure.description('# 1. Verify that Create Booking -> Patch Request - Verify that firstName is updated.')
@allure.tag("regression", 'smoke')
@allure.label("TC#1")

def test_patch_request(create_token,create_booking):
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"+str(create_booking)
    PATCH_URL = base_url+base_path

    cookie = "token=" + create_token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }
    json_payload = {
        "firstname": "Lakshya",
        }
    response = requests.patch(url=PATCH_URL, headers=headers, json=json_payload)
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data["firstname"] == "Lakshya"