import pytest
from test_cases.auth import AuthData
from api_client.auth_client import login_client
@pytest.mark.parametrize("data",AuthData.login_validation)
def test_login_success(data):
    response=login_client(data)
    assert response.status_code == 200
    assert "access_token" in response.json()
def test_login_invalid_password():
    data=AuthData.login_invalid_password
    response=login_client(data)
    assert response.status_code == 401
    assert "message" in response.json()
    assert response.json()["message"]=="password is invalid"
def test_login_invalid_email():
    data=AuthData.login_invalid_email
    response=login_client(data)
    assert response.status_code == 401
    assert "message" in response.json()
    assert response.json()["message"]=="email not found"
def test_login_missing_email():
    data=AuthData.login_invalid_email
    response=login_client(data)
    assert response.status_code == 422
    assert "message" in response.json()
def test_login_missing_password():
    data=AuthData.login_missing_password
    response=login_client(data)
    assert response.status_code == 422
    assert "message" in response.json()