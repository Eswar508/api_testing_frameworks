from test_cases.auth import AuthData
from api_client.auth_client import login_client,register_client
from utils.schema import LoginSchema,StudentSchema
def test_schema_login_response():
    login_data=AuthData.login_validation
    login_response=login_client(login_data)
    json_response=login_response.json()
    try:
        LoginSchema(**json_response)
        assert True
    except:assert False
def test_schema_signup_response():
    signup_data=AuthData.new_student_signup
    signup_response=register_client(signup_data)
    json_response=signup_response.json()
    try:
        StudentSchema(**json_response)
        assert True
    except:assert False