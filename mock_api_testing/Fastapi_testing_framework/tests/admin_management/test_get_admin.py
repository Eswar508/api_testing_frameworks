import pytest
from test_cases.admin_data import AdminData
from api_client.admin_client import get_admin_account
@pytest.mark.parametrize(("id","expected_data"),AdminData.admin_ids())
def test_admin_get_by_id(id,expected_data,admin_token):
    get_response=get_admin_account(admin_token,id)
    assert get_response.status_code==200
    json_response=get_response.json()
    assert json_response["name"]==expected_data["name"]
    assert json_response["email"]==expected_data["email"]
    assert json_response["user_id"]==expected_data["user_id"]
