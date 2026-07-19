from api_client.auth_client import login_client
import jwt
def get_token(data):
    r=login_client(data)
    return r.json()["access_token"]
def get_token_data(data):
    SECRET_KEY="my_secrete_token_key"
    ALGORITHM="HS256"
    token=get_token(data)
    data=jwt.decode(token,SECRET_KEY,ALGORITHM)
    return data