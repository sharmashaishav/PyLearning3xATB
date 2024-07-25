import pytest
import allure
import requests


@allure.title('Test POST Request = Restful Booker Project-1')
@allure.description('Test Case to verify that POST request works')
@allure.tag("regression", 'smoke')
@allure.label("TC#1")
def test_create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Anant",
        "lastname": "Ambani",
        "totalprice": 1129103981092831,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2023-01-01",
            "checkout": "2024-01-01"
        },
        "additionalneeds": "Breakfast,Dinner"
    }
    response = requests.post(url=URL,json=payload,headers=headers)
    assert response.status_code == 200

    responseData = response.json()

    assert responseData["bookingid"] is not None
    assert responseData["bookingid"] > 0
    assert type(responseData["bookingid"]) == int
    fname = responseData["booking"]["firstname"]
    check_in_date = responseData["booking"]["bookingdates"]["checkin"]
    assert fname == "Anant"
    assert check_in_date == "2023-01-01"


@allure.title('Test POST Request = Restful Booker Project-1_Negative Scenario-1')
@allure.description('Test Case to verify that POST request works')
@allure.label("TC#2")
def test_create_booking_no_payload():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking"
    URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {}
    response = requests.post(url=URL,json=payload,headers=headers)
    assert response.status_code == 500
    

