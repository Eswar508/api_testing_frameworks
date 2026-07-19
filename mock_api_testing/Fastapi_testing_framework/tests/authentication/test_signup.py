import pytest
from test_cases.auth import AuthData
from api_client.auth_client import register_client
@pytest.mark.parametrize("data",AuthData.new_student)
def test_signup_success(data):
    response=register_client(data)
    assert response.status_code == 201
    response_data = response.json()
    assert "user_id" in response_data
    assert response_data["email"] == data["email"]
def test_signup_duplicate_email():
    data = AuthData.duplicate_email
    response = register_client(data)
    assert response.status_code == 409 
    assert "message" in response.json()
    assert response.json()["message"] == "email already exists"
def test_signup_invalid_email():
    data = AuthData.invalid_email
    response = register_client(data)
    assert response.status_code == 422
def test_signup_invalid_name():
    data = AuthData.invalid_name
    response = register_client(data)
    assert response.status_code == 422
def test_signup_missing_email():
    data = AuthData.missing_email
    response = register_client(data)
    assert response.status_code == 422
def test_signup_missing_password():
    data = AuthData.missing_password
    response = register_client(data)
    assert response.status_code == 422