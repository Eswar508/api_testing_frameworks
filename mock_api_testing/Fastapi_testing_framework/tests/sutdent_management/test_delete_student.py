import pytest
from test_cases.student_data import StudentData
from api_client.student_client import delete_student_account
def test_delete_student_by_id(admin_token):
    id=StudentData.deleted_id2
    delete_response=delete_student_account(admin_token,id)
    assert delete_response.status_code==204
    assert "message" in delete_response.json()
def test_delete_student_by_invalid_id(id,admin_token):
    id=StudentData.invalid_id
    delete_response=delete_student_account(admin_token,id)
    assert delete_response.status_code==204
def test_delete_student_by_deleted_id(admin_token,deleted_id):
    delete_response=delete_student_account(admin_token,deleted_id)
    assert delete_response.status_code==404
