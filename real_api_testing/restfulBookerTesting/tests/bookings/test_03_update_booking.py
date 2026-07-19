import pytest
from pages.execute import Execute_with_data
from utils.test_cases import test_cases
import allure
@allure.epic("update data")
@allure.feature("put data")
@pytest.mark.update_booking
def test_update_booking(booking_client,id=test_cases.update()):
    allure.dynamic.title(f"updating the id {id}")
    allure.dynamic.description(f"updating the data of id {id} with new data")
    payload={"firstname":"updated_name","lastname":"updated_lastname","totalprice":123,"depositpaid":True,"bookingdates":{"checkin":"2024-01-01","checkout":"2024-01-10"},"additionalneeds":"updated_needs"}
    with allure.step("saving data"):
        exe=Execute_with_data(booking_client,data=payload,code=200,id=id)
    with allure.step("validating the resoponse"):
        exe.update_response_Test()