from testing_framework.clients.auth_client import login_client
import pytest
from flask_api.helper_fun import token_data
import testing_framework.test_cases.login as t
from flask_api.data_base.data_services.users_service import get_user_by_email
@pytest.mark.parametrize("login_data",t.data)
def test_valid_login(login_data):
    login_response=login_client(login_data)
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()
    assert "user" in login_response.json()
    user=login_response.json()["user"]
    #verify data base
    db_data=get_user_by_email(login_data["email"])
    assert user["name"]==db_data.name
    assert user["email"]==db_data.email
def test_invalid_email():
    invalid_email=t.invalid_email
    login_response=login_client(invalid_email)
    assert login_response.status_code == 401
def test_invalid_password():
    invalid_password=t.invalid_password
    login_response=login_client(invalid_password)
    assert login_response.status_code == 422
def test_missing_email():
    missing_email=t.missing_email
    login_response=login_client(missing_email)
    assert login_response.status_code == 422
def test_missing_password():
    missing_password=t.missing_password
    login_response=login_client(missing_password)
    assert login_response.status_code == 422
def test_user_not_found():
    non_existing_user=t.non_existing_user
    login_response=login_client(non_existing_user)
    assert login_response.status_code == 401
def test_login_returns_valid_jwt():
    user=t.valid_user
    login_response=login_client(user)
    assert login_response.status_code == 200
    assert "access_token" in login_response.json()
    expected_data=get_user_by_email(user["email"])
    tokendata=token_data(login_response.json()["access_token"])
    assert tokendata["iat"]<tokendata["exp"]
    assert tokendata["role"]==expected_data.role
    assert tokendata["user_id"]==expected_data.user_id
    
    