import pytest
from test_cases.student_data import StudentData
from api_client.student_client import update_student_account
def test_update_student_me(student_update_token):
    payload=StudentData.update_me
    patch_response=update_student_account(student_update_token,payload)
    assert patch_response.status_code==200
def test_update_student_invalid_name(student_update_token):
    payload=StudentData.update_invalid_name
    patch_response=update_student_account(student_update_token,payload)
    assert patch_response.status_code==200
def test_update_student_invalid_email(student_update_token):
    payload=StudentData.update_invalid_email
    patch_response=update_student_account(student_update_token,payload)
    assert patch_response.status_code==200
def test_update_student_duplicate_name(student_update_token):
    payload=StudentData.update_duplicate_name
    patch_response=update_student_account(student_update_token,payload)
    assert patch_response.status_code==200
