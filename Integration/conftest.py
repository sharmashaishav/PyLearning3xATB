import os

import pytest
import requests
from dotenv import load_dotenv
@pytest.fixture()
def create_booking():
    base_url = "https://restful-booker.herokuapp.com"
    base_path = "/booking/"
    booking_URL = base_url + base_path
    headers = {"Content-Type": "application/json"}
    payload = {
        "firstname": "Lakshay",
        "lastname": "Sen",
        "totalprice": 112910398131,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-07-01",
            "checkout": "2024-08-01"
        },
        "additionalneeds": "Breakfast,Dinner,Badminton Court"
    }
    response = requests.post(url=booking_URL,json=payload,headers=headers)
    assert response.status_code == 200
    # print(response.json())

    Booking_id = response.json()["bookingid"]
    print(Booking_id)
    return Booking_id


@pytest.fixture()
def create_token():
    load_dotenv()
    url = os.getenv("A_URL")
    uname = os.getenv("username")
    pswd = os.getenv("password")
    headers = {"Content-Type": "application/json"}
    json_payload = {
        "username": "admin",
        "password": "password123"
          }
    response = requests.post(url=url, headers=headers, json=json_payload)
    token = response.json()["token"]
    print(token)
    return token
