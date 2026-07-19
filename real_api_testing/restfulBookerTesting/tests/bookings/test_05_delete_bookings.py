import pytest
from pages.execute import Execute_with_data
from utils.test_cases import test_cases
import allure
@allure.epic("delete")
@allure.feature("correct id")
@allure.story("delete valid id")
@pytest.mark.delete_booking
@pytest.mark.parametrize("id",test_cases.delete())
def test_delete_booking(booking_client,id):
    allure.dynamic.title(f"delete id {id}")
    allure.dynamic.description(f"deleting the id {id} to check if the status code is 201 and a json message confirming the id is deleted")
    with allure.step("saving meta data"):
        exe=Execute_with_data(booking_client,code=201,id=id)
    with allure.step("validating response of delete method against expected"):
        exe.delete_response_Test()
@allure.epic("delete")
@allure.feature("incorrect id")
@allure.story("delete non existent id")
@pytest.mark.delete_booking
def test_delete_non_existent_booking(booking_client):
    allure.dynamic.title(f"try to delete non existent id {id}")
    allure.dynamic.description(f"trying to delete non existent id {id} to check if the status code is 405 and a json message confirming that deleting failed")
    with allure.step("saving meta data"):
        exe=Execute_with_data(booking_client,code=405,id=99999)
    with allure.step("validating response"):
        exe.delete_response_Test()
@allure.epic("delete")
@allure.feature("incorrect id")
@allure.story("delete deleted id")
@pytest.mark.delete_booking
def test_delete_deletedBooking(booking_client,id=test_cases.deleted0()):
    allure.dynamic.title(f"try to delete deleted id {id}")
    allure.dynamic.description(f"trying to delete deleted id {id} to check if the status code is 405 and a json message confirming that  deleting failed")
    with allure.step("saving meta data"):
        exe=Execute_with_data(booking_client,code=405,id=id)
    with allure.step("validating response"):
        exe.delete_response_Test()
@allure.epic("get data")
@allure.feature("deleted id")
@pytest.mark.delete_booking
def test_get_deleted_booking(booking_client,id=test_cases.deleted1()):
    allure.dynamic.title(f"get deleted  id {id}")
    allure.dynamic.description(f"trying to get deleted id {id} to check if the status code is 404 and a json message confirming that failed getting the id")
    with allure.step("saving meta data"):
        exe=Execute_with_data(booking_client,code=404,id=id)
    with allure.step("validating response"):
        exe.get_response_Test()