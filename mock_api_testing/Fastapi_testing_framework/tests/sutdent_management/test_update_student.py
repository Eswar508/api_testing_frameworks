from test_cases.student_data import StudentData
from api_client.student_client import update_student_account
def test_update_by_id(admin_token):
    payload=StudentData.id_update
    id=StudentData.update_id
    patch_response=update_student_account(admin_token,payload,id)
    assert patch_response.status_code==200
    json_response=patch_response.json()
    assert json_response["name"]==payload["name"]
def test_update_invalid_name(admin_token):
    payload=StudentData.id_update_invalid_name
    id=StudentData.update_id
    patch_response=update_student_account(admin_token,payload,id)
    assert patch_response.status_code==200
def test_update_invalid_email(admin_token):
    id=StudentData.update_id
    payload=StudentData.id_update_invalid_email
    patch_response=update_student_account(admin_token,payload,id)
    assert patch_response.status_code==200
def test_update_duplicate_name(admin_token):
    id=StudentData.update_id
    payload=StudentData.id_update_duplicate_name
    patch_response=update_student_account(admin_token,payload,id)
    assert patch_response.status_code==200
