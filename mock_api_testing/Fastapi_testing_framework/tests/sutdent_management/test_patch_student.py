from test_cases.student_data import StudentData
from api_client.student_client import patch_student_account
def test_patch_student_name(admin_token):
    id=StudentData.patch_id
    payload=StudentData.id_patch_name
    patch_response=patch_student_account(admin_token,payload,id)
    assert patch_response.status_code==200
    json_response=patch_response.json()
    assert json_response["name"]==payload["name"]
def test_patch_student_email(payload,admin_token):
    id=StudentData.patch_id
    payload=StudentData.id_patch_email
    patch_response=patch_student_account(admin_token,payload,id)
    assert patch_response.status_code==200
    json_response=patch_response.json()
    assert json_response["email"]==payload["email"]
def test_patch_student_multiple_fields(admin_token):
    id=StudentData.update_id
    payload=StudentData.id_pathc_multi
    patch_response=patch_student_account(admin_token,payload,id)
    assert patch_response.status_code==200
    json_response=patch_response.json()
    assert json_response["name"]==payload["name"]
    assert json_response["age"]==payload["age"]
def test_patch_student_invalid_name(admin_token):
    id=StudentData.update_id
    payload=StudentData.id_patch_invalid_name
    patch_response=patch_student_account(admin_token,payload,id)
    assert patch_response.status_code==200
    json_response=patch_response.json()
def test_patch_student_invalid_email(admin_token):
    id=StudentData.update_id
    payload=StudentData.id_patch_invalid_email
    patch_response=patch_student_account(admin_token,payload,id)
    assert patch_response.status_code==200
    json_response=patch_response.json()
def test_patch_student_duplicate_name(admin_token):
    id=StudentData.update_id
    payload=StudentData.id_patch_duplicate_name
    patch_response=patch_student_account(admin_token,payload,id)
    assert patch_response.status_code==200

