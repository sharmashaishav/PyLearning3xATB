import os
import dotenv
import allure
import pytest
import requests

@allure.title('Integration Scenario-2')
@allure.description('# 2. Create a Booking, Delete the Booking with ID and Verify using GET request that it should not exist.')
@allure.tag("regression", 'smoke')
@allure.label("TC#2")

def test_Delete_with_ID(create_token, create_booking):

    Booking_URL = os.getenv("B_URL")
    Delete_URL = Booking_URL + str(create_booking)

    cookie = "token=" + create_token

    headers = {
        "Content-Type": "application/json",
        "Cookie": cookie
    }

    # We'll first verify the record
    response = requests.get(url=Delete_URL, headers=headers)
    responseData = response.json()
    print(responseData)

    # Now We will DELETE that record
    response = requests.delete(url=Delete_URL,headers=headers)
    assert response.status_code == 201

    # Now we will again verify if record is deleted or not
    response = requests.get(url=Delete_URL)
    # responseData = response.json()
    # print(responseData)
    assert response.status_code == 404



