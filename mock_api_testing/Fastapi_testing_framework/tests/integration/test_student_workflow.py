import pytest
from test_cases.auth import AuthData
from test_cases.student_data import StudentData
from api_client.student_client import *
from api_client.auth_client import login_client
def test_student_workflow():
    login_data=AuthData.login_student_workflow2
    #login student with data
    login_response=login_client(login_data)
    assert login_response.status_code==200
    assert "access_data" in login_response.json()
    token=login_response.json()["access_data"]
    #get student data via id
    id=login_response.json()["user"]["user_id"]
    get_response=get_student_account(token,id)
    assert get_response.status_code==200
    assert get_response.json()["name"] == login_response.json()["user"]["name"]
    assert get_response.json()["email"] == login_response.json()["user"]["email"]
    #update the students data with the given payload
    payload=StudentData.student_workflow_update
    patch_response=patch_student_account(token,id,payload)
    assert patch_response.status_code==200
    assert patch_response.json()["name"]==payload["name"]
    assert patch_response.json()["email"]==payload["email"]
    #verify the updated data by getting the students data
    get_response_path=get_student_account(token,id)
    assert get_response_path.status_code==200
    assert get_response_path.json()["name"]==payload["name"]
    assert get_response_path.json()["email"]==payload["email"]
    #delete the student from the data base
    delete_response=delete_student_account(token,id)
    assert delete_response.status_code == 204
    #verify student deletion
    get_response_delete=get_student_account(token,id)
    assert get_response_delete.status_code==404
    