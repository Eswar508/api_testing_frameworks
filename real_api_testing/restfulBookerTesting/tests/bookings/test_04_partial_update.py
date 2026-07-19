import pytest
from pages.execute import Execute_with_data
from utils.test_cases import test_cases
import allure
@allure.epic("update data")
@allure.feature("patch data")
@pytest.mark.partial_update_booking
def test_partial_update_booking(booking_client,id=test_cases.partial_update()):
    payload={"firstname":"updated_name"}
    allure.dynamic.title(f"patching the id {id}")
    allure.dynamic.description(f"patching the fields of data of id {id} with one")
    with allure.step("saving meta data"):
        exe=Execute_with_data(booking_client,code=200,id=id,data=payload)
    with allure.step("validating response"):
        exe.partial_update_response_Test()