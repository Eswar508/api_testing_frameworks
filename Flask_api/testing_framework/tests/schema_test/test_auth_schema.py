from testing_framework.clients.auth_client import *
from testing_framework.utils.validate_schema import validate_login_schema,validate_token_schema
import testing_framework.test_cases.login as test_cases
from flask_api.helper_fun import token_data
def test_login_response_schema():
    payload=test_cases.valid_user
    response=login_client(payload)
    assert response.status_code == 200
    assert validate_login_schema(response.json())
def test_token_data_schema():
    payload=test_cases.valid_user
    response=login_client(payload)
    assert response.status_code == 200
    assert "access_token" in response.json()
    tokendata=token_data(response.json()["access_token"])
    assert validate_token_schema(tokendata)