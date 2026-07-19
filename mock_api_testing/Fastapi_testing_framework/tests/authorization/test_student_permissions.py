import pytest
from test_cases.student_data import StudentData
from test_cases.admin_data import AdminData
from api_client.student_client import *
def test_student_access_own_account(student_token):
    response=get_student_account(student_token)
    assert response.status_code==200
def test_student_update_own_account(student_token):
    payload=StudentData.self_update_permission
    response=update_student_account(student_token,payload)
    response.status_code==200
    response.json()["name"]==payload["name"]
    response.json()["email"]==payload["email"]
def test_student_delete_own_account():
    token=StudentData.delete_token1()
    response=delete_student_account(token)
    response.status_code==200
def test_student_access_own_account_by_id(student_token):
    id=StudentData.own_id
    response=get_student_account(student_token,id)
    assert response.status_code==200
def test_student_cannot_access_other_students(student_token):
    id=StudentData.student_id2
    response=get_student_account(student_token,id)
    assert response.status_code==200
def test_student_cannot_delete_other_students(student_token):
    id=StudentData.delete_id1
    response=delete_student_account(student_token,id)
    response.status_code==200
def test_student_cannot_update_other_students(student_token):
    id=StudentData.update_id
    payload=StudentData.other_update_permission
    response=update_student_account(student_token,id,payload)
    response.status_code==200
    response.json()["name"]==payload["name"]
    response.json()["email"]==payload["email"]
def test_student_cannot_access_admins(student_token):
    id=AdminData.other_admin_id
    response=get_student_account(student_token,id)
    response.status_code==200