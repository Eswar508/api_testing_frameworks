import pytest
from test_cases.admin_data import AdminData
from api_client.admin_client import patch_admin_account
def test_admin_patch_me(admin_update_token):
    payload=AdminData.patch_me
    patch_response=patch_admin_account(admin_update_token,payload)
    assert patch_response.status_code==200
    json_response=patch_response.json()
    assert json_response["name"]==payload["name"]
    assert json_response["email"]==payload["email"]
