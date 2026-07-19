import pytest
from test_cases.admin_data import AdminData
from utils.schema import AdminSchema
from api_client.admin_client import *
@pytest.mark.parametrize(("id","expected_data"),AdminData.admin_ids())
def test_schema_admin_get_by_id(id,admin_token,expected_data):
    get_response=get_admin_account(admin_token,id)
    json_response=get_response.json()
    try:
        AdminSchema(**json_response)
        assert True
    except:assert False
def test_schema_admin_get_me(admin_token):
    get_response=get_admin_account(admin_token)
    json_response=get_response.json()
    try:
        AdminSchema(**json_response)
        assert True
    except:assert False
def test_schema_admin_patch_me(admin_update_token):
    payload=AdminData.patched_schema
    patch_response=patch_admin_account(admin_update_token,payload)
    json_response=patch_response.json()
    try:
        AdminSchema(**json_response)
        assert True
    except:assert False
def test_schema_admin_update_me(admin_update_token):
    payload=AdminData.updated_schema
    patch_response=update_admin_account(admin_update_token,payload)
    json_response=patch_response.json()
    try:
        AdminSchema(**json_response)
        assert True
    except:assert False