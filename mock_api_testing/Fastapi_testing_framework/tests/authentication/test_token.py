from test_cases.auth import AuthData
from api_client.student_client import get_student_account
from utils.helper_fun import get_token_data
def test_access_with_valid_student_token(student_token):
    response=get_student_account(student_token)
    token_data=get_token_data(student_token)
    assert response.status_code==200
    assert response.json()["user_id"]==token_data["user_id"]
def test_access_without_token():
    response=get_student_account()
    assert response.status_code==401
def test_access_with_invalid_token():
    invalid_token=AuthData.tokens["invalid_token"]
    response=get_student_account(invalid_token)
    assert response.status_code==401
def test_malformed_token():
    malformed_token=AuthData.tokens["malformed_token"]
    response=get_student_account(malformed_token)
    assert response.status_code==401
def test_access_with_expired_token():
    expired_token=AuthData.tokens["expired_token"]
    response=get_student_account(expired_token)
    assert response.status_code==401
