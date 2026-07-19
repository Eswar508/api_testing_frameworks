from test_cases.auth import AuthData
from test_cases.student_data import StudentData
from test_cases.admin_data import AdminData
from api_client.admin_client import *
from api_client.student_client import *
from api_client.auth_client import login_client
def test_admin_student_workflow():
    #login student with email
    login_data=AuthData.login_student_workflow1
    login_response=login_client(login_data)
    login_response_json=login_response.json()
    assert login_response.status_code==200
    assert "access_token" in login_response_json
    token=login_response_json["access_token"]
    assert "user_id" in login_response_json["user"]
    #get data of the student via id
    id=login_response_json["user"]["user_id"]
    get_response=get_student_account(token,id)
    assert get_response.status_code==200
    assert get_response.json()["name"] == login_response_json["user"]["name"]
    assert get_response.json()["email"] == login_response_json["user"]["email"]
    #update the students data with the given payload
    payload=StudentData.admin_workflow_update
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
    
def test_admin_workflow():
    login_data=AuthData.login_admin_workflow
    #login admin with email and password
    login_response=login_client(login_data)
    assert login_response.status_code==200
    assert "access_token" in login_response.json()
    token=login_response["access_token"]
    get_response=get_admin_account(token)    
    assert get_response.status_code ==200
    assert get_response.json()["name"]==login_response["user"]["name"]
    assert get_response.json()["email"]==login_response["user"]["email"]
    payload=AdminData.workflow_update
    patch_response=patch_admin_account(token,payload)
    assert patch_response.status_code==200
    assert patch_response.json()["name"]==payload["name"]
    assert patch_response.json()["email"]==payload["email"]
    