import os
import dotenv
import allure
import pytest
import requests
@allure.title('Integration Scenario-3')
@allure.description('# 3. Get an Existing Booking id from Get All Bookings Ids , Update a Booking and Verify using GET by id.')
@allure.tag("regression", 'smoke')
@allure.label("TC#3")

def test_GET_ALL_BOOKINGS(create_token):
    GET_URL = "https://restful-booker.herokuapp.com/booking/"
    cookie = "token=" + create_token
    headers = {"Content-Type": "application/json","Cookie": cookie}
    response = requests.get(url=GET_URL,headers=headers)
    assert response.status_code == 200
    ALL_BOOKINGS = response.json()
    booking_id = ALL_BOOKINGS[21]["bookingid"]
    print("\nBooking ID to be updated -->",booking_id)

    # USING PATCH METHOD UPDATE THE BOOKING DETAILS
    updated_url = GET_URL + str(booking_id)
    payload = {
        "firstname": "Virat",
        "lastname": "Kohli"
    }

    updatedResponse = requests.patch(url=updated_url,headers=headers,json=payload)
    assert response.status_code == 200
    print('\nUpdating the Booking')

    # USING GET METHOD VERIFY THE UPDATE
    getUpdatedResponse = requests.get(url=updated_url,headers=headers)
    getUpdatedResponseData = getUpdatedResponse.json()
    assert getUpdatedResponseData["firstname"] == "Virat"
    assert getUpdatedResponseData["lastname"] == "Kohli"
    print('\nBooking Updated successfully')