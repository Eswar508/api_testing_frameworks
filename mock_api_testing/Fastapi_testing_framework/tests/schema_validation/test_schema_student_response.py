import pytest
from test_cases.student_data import StudentData
from api_client.student_client import *
from utils.schema import StudentSchema
@pytest.mark.parametrize(("id","expected_data"),StudentData.student_id())
def test_get_student_by_id(id,admin_token,expected_data):
    get_response=get_student_account(admin_token,id)
    json_response=get_response.json()
    try:
        StudentSchema(**json_response)
        assert True
    except:assert False
def test_get_student_me(student_token):
    get_response=get_student_account(student_token)
    json_response=get_response.json()
    try:
        StudentSchema(**json_response)
        assert True
    except:assert False
def test_patch_student_name_by_id(admin_token):
    payload=StudentData.patched_schema
    id=StudentData.patch_id
    patch_response=patch_student_account(admin_token,payload,id)
    json_response=patch_response.json()
    try:
        StudentSchema(**json_response)
        assert True
    except:assert False
def test_patch_me_student_name(student_update_token):
    payload=StudentData.schema_patch_me
    patch_response=patch_student_account(student_update_token,payload)
    json_response=patch_response.json()
    try:
        StudentSchema(**json_response)
        assert True
    except:assert False
def test_update_me_student(student_update_token):
    payload=StudentData.schema_update_me
    patch_response=update_student_account(student_update_token,payload)
    json_response=patch_response.json()
    try:
        StudentSchema(**json_response)
        assert True
    except:assert False
def test_update_student_by_id(admin_token):
    payload=StudentData.updated_schema
    id=StudentData.update_id
    patch_response=update_student_account(admin_token,payload,id)
    json_response=patch_response.json()
    try:
        StudentSchema(**json_response)
        assert True
    except:assert False