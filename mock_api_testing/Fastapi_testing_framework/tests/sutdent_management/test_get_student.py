import pytest
from test_cases.student_data import StudentData
from api_client.student_client import get_student_account
@pytest.mark.parametrize(("id","expected_data"),StudentData.student_id())
def test_get_student_by_id(id,expected_data,admin_token):
    get_response=get_student_account(admin_token,id)
    assert get_response.status_code==200
    json_response=get_response.json()
    assert json_response["name"]==expected_data["name"]
    assert json_response["email"]==expected_data["email"]
    assert json_response["user_id"]==expected_data["user_id"]

def test_get_student_by_invalid_id(admin_token):
    id=StudentData.invalid_id
    get_response=get_student_account(admin_token,id)
    assert get_response.status_code==200

def test_get_student_by_deleted_id(admin_token,deleted_id):
    get_response=get_student_account(admin_token,deleted_id)
    assert get_response.status_code==200

