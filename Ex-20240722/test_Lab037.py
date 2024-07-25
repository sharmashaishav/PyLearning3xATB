import pytest
import allure


@allure.title("TC_1 - verify that 2-2 is 0")
@allure.description("This is a smoke test case to verify that 2-2 is 0")
@pytest.mark.smoke
def test_sub():
    assert 2 - 2 == 0


@allure.title("TC_2 - verify that 3+4 is 7")
@allure.description("This is a smoke test case to verify that 3+4 is 7")
@pytest.mark.smoke
def test_add():
    assert 3 + 4 == 7
