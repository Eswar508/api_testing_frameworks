import pytest
from api_client.auth_client import *
from api_client.student_client import delete_student_account
from api_client.auth_client import login_client
from utils.helper_fun import get_token
@pytest.fixture(scope="session")
def admin_update_token():
    data={"email":"admin2@gmail.com","password":"$AnAdmin2"}
    return get_token(data)
@pytest.fixture(scope="session")
def student_update_token():
    data={"email":"student4@gmail.com","password":"$Student4"}
    return get_token(data)
@pytest.fixture(scope="session")
def admin_token():
    data={"email":"admin1@gmail.com","password":"$AnAdmin1"}
    return get_token(data)
@pytest.fixture(scope="session")
def student_token():
    data={"email":"student1@gmail.com","password":"$Student1"}
    return get_token(data)
@pytest.fixture(scope="function")
def deleted_id(admin_token):
    id=12
    delete_student_account(admin_token,id)
    return id
@pytest.fixture(scope="function")   
def deleted_token():
    payload={
            "email":"student9@gmail.com",
            "password":"$Student9"
        }
    token=get_token(payload)
    delete_student_account(token)
    return token