import pytest
import allure
import requests

@allure.title('Test GET Request = Restful Booker Project-1')
@allure.description('Test Case 1 to verify that GET request with Booking ID works')
@allure.tag("regression",'smoke')
@allure.label("TC#1")
@pytest.mark.smoke
def test_get_request_by_booking_id():
    url="https://restful-booker.herokuapp.com/booking/1"
    responseData = requests.get(url)
    print(responseData.json())
    print(responseData.text)
    print(responseData.headers)
    print(responseData.cookies)
    assert responseData.status_code == 200

@allure.title('Test GET Request = Restful Booker Project-1')
@allure.description('Test Case 2 to verify that GET request with invalid Booking ID')
@allure.tag("regression",'smoke')
@allure.label("TC#2")
@pytest.mark.smoke
def test_Negative_request_by_booking_id():
    url="https://restful-booker.herokuapp.com/booking/invalid"
    responseData = requests.get(url)
    assert responseData.status_code == 404