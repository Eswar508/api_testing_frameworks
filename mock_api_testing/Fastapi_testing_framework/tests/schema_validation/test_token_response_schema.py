from test_cases.auth import AuthData
from utils.helper_fun import get_token_data
from api_client.auth_client import login_client
def test_schema_token_data():
    login_data=AuthData.login_validation
    token_data=get_token_data(login_data)