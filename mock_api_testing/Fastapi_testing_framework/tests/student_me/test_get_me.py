import pytest
from api_client.admin_client import get_admin_account
from test_cases.student_data import StudentData
@pytest.mark.parametrize(("token","expecte_data"),StudentData.student_token())
def test_get_student_me(expected_data,token):
    get_response=get_admin_account(token)
    assert get_response.status_code==200
    json_response=get_response.json()
    assert json_response["name"]==expected_data["name"]
    assert json_response["email"]==expected_data["email"]
    assert json_response["user_id"]==expected_data["user_id"]