import json
import datetime
import jwt
id_path=r"FastApi\storage\user_ids.json"
password_path=r"FastApi\storage\user_passwords.json"
def get_data(path):
    with open(path) as f:
        return json.load(f)
def post_data(path,data):
    with open(path,"w") as f:
        json.dump(data,f,indent=5)
def save_new_id():
    ids=get_data(id_path)
    new_id=max(ids)+1
    ids.append(new_id)
    post_data(id_path,ids)
    return new_id
def remove_id(id):
    ids=get_data(id_path)
    ids.remove(id)
    post_data(id_path,ids)
def save_password(password,id):
    storage=get_data(password_path)
    storage[str(id)]=password
    post_data(password_path,storage)
def remove_password(id):
    storage=get_data(password_path)
    del storage[str(id)]
    post_data(password_path,storage)
def generate_login_response(data):
    id=data["user_id"]
    role="admin" if id<=5 else "student"
    payload={
        "user_id":data["user_id"],
        "iat":datetime.datetime.now(datetime.timezone.utc),
        "exp":datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(hours=1),
        "role":role
    }
    SECRET_KEY="my_secrete_token_key"
    ALGORITHM="HS256"
    Token=jwt.encode(payload,SECRET_KEY,ALGORITHM)
    response={
        "access_token":Token,
        "token_type":"Bearer",
        "user":{
            "user_id":id,
            "name":data["name"],
            "email":data["email"]
        }
    }
    return response
class APIException(Exception):
    def __init__(self, message : str,status_code : int):
        self.message = message
        self.status_code=status_code
