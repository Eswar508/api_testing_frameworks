import pytest
from test_cases.admin_data import AdminData
from api_client.admin_client import get_admin_account
@pytest.mark.parametrize(("token","expected_data"),AdminData.admin_token())
def test_admin_get_me(token,expected_data):
    get_response=get_admin_account(token)
    assert get_response.status_code==200
    json_response=get_response.json()
    assert json_response["name"]==expected_data["name"]
    assert json_response["email"]==expected_data["email"]
    assert json_response["user_id"]==expected_data["user_id"]

