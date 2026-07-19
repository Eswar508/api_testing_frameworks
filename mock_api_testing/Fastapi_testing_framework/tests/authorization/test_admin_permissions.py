import pytest
from test_cases.student_data import StudentData
from test_cases.admin_data import AdminData
from api_client.admin_client import get_admin_account,update_admin_account
from api_client.student_client import get_student_account,patch_student_account
@pytest.mark.parametrize("id",StudentData.student_id2)
def test_admin_access_any_student(id,admin_token):
    response=get_student_account(admin_token,id)
    response.status_code==200
@pytest.mark.parametrize("id",StudentData.update_id)
def test_admin_patch_any_students(admin_token,id):
    payload=StudentData.admin_patch_permission
    response=patch_student_account(admin_token,payload,id)
    response.status_code==200
    response.json()["name"]==payload["name"]
    response.json()["email"]==payload["email"]
@pytest.mark.parametrize("id",AdminData.other_admin_id)
def test_admin_access_other_admins(admin_token,id):
    response=get_admin_account(admin_token,id)
    response.status_code==200
def test_admin_access_own_account(admin_token):
    response=get_admin_account(admin_token)
    response.status_code==200
def test_admin_updates_own_account(admin_update_token):
    payload=AdminData.update_permisssion
    response=update_admin_account(admin_update_token,payload)
    response.status_code==200
    response.json()["name"]==payload["name"]
    response.json()["email"]==payload["email"]