import pytest
from pages.execute import Execute_with_data
from utils.test_cases import test_cases
import allure
@allure.epic("get data")
@allure.feature("get valid id")
@pytest.mark.get_booking
@pytest.mark.parametrize(("id,data"),test_cases.get())
def test_get_booking(booking_client,id,data):
    allure.dynamic.title(f"get valid id {id}")
    allure.description("get data that is posted with valid id and expect the valid response code 200")
    with allure.step("save meta data"):
        exe=Execute_with_data(booking_client,code=200,data=data,id=id)
    with allure.step("validating the response code"):
        exe.get_response_Test()
@allure.epic("get data")
@allure.feature("get invalid id")
@pytest.mark.get_booking                                                                                                        
def test_get_non_existent_booking(booking_client):
    allure.dynamic.title("get non existent booking")
    allure.description("get non existent id and check is the status code is 404")
    with allure.step("save meta data"):
        exe=Execute_with_data(booking_client,code=404,id=99999)
    with allure.step("validate status code"):
        exe.get_response_Test()
@allure.epic("get data")
@allure.feature("get invalid id")
@pytest.mark.get_booking
def test_get_booking_invalid_id(booking_client):
    allure.dynamic.title("get invalid data")
    allure.description("checking wheather the response is 404 for getting with invalid id")
    with allure.step("save data"):
        exe=Execute_with_data(booking_client,code=404,id="invalid_id")
    with allure.step("validate status code"):
        exe.get_response_Test()