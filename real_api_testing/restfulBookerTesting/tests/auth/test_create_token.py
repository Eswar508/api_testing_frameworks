import pytest
from utils.assertions import validate
from utils.test_cases import test_cases
import allure
@allure.epic("Authentication")
@allure.feature("Generate Token")
def test_generate_token(auth_client):
    data=test_cases.login()
    allure.dynamic.title(f"Testing with {data["username"]}")
    allure.dynamic.description(f"testing with valid user name {data["username"]} whose results to be expected with status code 200 and token in json body as any string")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    with allure.step("obtaining token"):
        response=auth_client.generate_token(data)
        assert_True=validate(response)
    with allure.step("checking status code"):
        assert_True.if_status_code(200)
    with allure.step("checking is it string"):
        assert_True.if_token_is_string()
@allure.epic("Authentication")
@allure.feature("Generate Token")
@pytest.mark.parametrize("test_case",test_cases.invalid_login())
def test_generate_token_with_invalid_data(auth_client,test_case):
    allure.dynamic.title(f"Testing with {test_case["username"]}")
    allure.dynamic.description(f"testing with invalid user name {test_case["username"]} whose results to be expected with status code 200 and absense of token in json body")
    allure.dynamic.severity(allure.severity_level.CRITICAL)
    with allure.step("obtaining token"):
        response=auth_client.generate_token(test_case)
        assert_True=validate(response)
    with allure.step("checking status code"):
        assert_True.if_status_code(200)
    with allure.step("checking absence of token"):
        assert_True.if_token_is_not_present()