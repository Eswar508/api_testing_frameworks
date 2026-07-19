import pytest
from test_cases.student_data import StudentData
from api_client.student_client import patch_student_account
def test_patch_student_name(student_update_token):
    payload=StudentData.patch_name
    patch_response=patch_student_account(student_update_token,payload)
    assert patch_response.status_code==200
    json_response=patch_response.json()
    assert json_response["name"]==payload["name"]
def test_patch_student_email(student_update_token):
    payload=StudentData.patch_email
    patch_response=patch_student_account(student_update_token,payload)
    assert patch_response.status_code==200
    json_response=patch_response.json()
    assert json_response["email"]==payload["email"]
def test_patch_student_multiple_fields(student_update_token):
    payload=StudentData.path_multi
    patch_response=patch_student_account(student_update_token,payload)
    assert patch_response.status_code==200
    json_response=patch_response.json()
    assert json_response["name"]==payload["name"]
    assert json_response["age"]==payload["age"]
def test_patch_student_invalid_name(student_update_token):
    payload=StudentData.patch_invalid_name
    patch_response=patch_student_account(student_update_token,payload)
    assert patch_response.status_code==200
def test_patch_student_invalid_email(student_update_token):
    payload=StudentData.patch_invalid_email
    patch_response=patch_student_account(student_update_token,payload)
    assert patch_response.status_code==200
def test_patch_student_duplicate_name(student_update_token):
    payload=StudentData.patch_duplicate_name
    patch_response=patch_student_account(student_update_token,payload)
    assert patch_response.status_code==422

