from fastapi import Depends
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
import jwt
from FastApi.utils.helper_fun import *
from pydantic import ValidationError
from  FastApi.validations.base_models import *
from FastApi.utils.helper_fun import *
security=HTTPBearer()
def verify_token(credentials : HTTPAuthorizationCredentials=Depends(security)):
    token=credentials.credentials
    try:
        token_data=jwt.decode(token,"my_secrete_token_key",algorithms=["HS256"])
        data=TokenModel(**token_data)
    except jwt.DecodeError:
        raise APIException(status_code=401, message="got malformed token")
    except jwt.ExpiredSignatureError:
        raise APIException(status_code=401, message="Token expired")
    except jwt.InvalidTokenError:
        raise APIException(status_code=401, message="Invalid token")
    except ValidationError:
        raise APIException(status_code=401,message="invalid token payload")
    except Exception as e:
        raise APIException(status_code=500,message=f"Internal server Error")
    return data.model_dump()
def get_data_with(data,field_name):
    path=r'FastApi\storage\user_registry.json'
    storage=get_data(path)
    for S in storage.values():
        if data[field_name] ==S[field_name] :return S
    return None
def duplicate_identity_field_verification(data):
    fields=[]
    if "name" in data and get_data_with(data,"name") :
        fields.append("name")
    if "email" in data and get_data_with(data,"email") :
        fields.append("email")
    if fields : raise APIException(status_code=409,message=f"{' and '.join(fields)} already exists")
def duplicate_identity_verification(data):
    path=r'FastApi\storage\user_registry.json'
    storage=get_data(path)
    result=[]
    for S in storage.values():
        name_exist=data["name"] ==S["name"]
        email_exist=data["email"] ==S["email"]
        if name_exist or email_exist:result.append(S)
    if result:
        if len(result)==1:
            if data["name"] == result[0]["name"]:
                raise APIException(status_code=409,message=f"the user name already exists")
            else:
                raise APIException(status_code=409,message=f"the user email already exists")
        raise APIException(status_code=409,message="the user name and email already exists")
def admin_verify(token):
    if token["role"] != "admin":
        raise APIException(status_code=403,message=f"student endpoint not for admin")
def student_verify(token_data):
    if token_data["role"] != "student":
        raise APIException(status_code=403,message=f"student endpoint not for admin")
def authorize_user(token_data,id):
    is_admin_id=(id<=5 and id>0)
    if is_admin_id :raise APIException(message="cannot access admin id via student endpoint",status_code=403)
    if token_data["role"]=="admin":return
    if token_data["user_id"] ==id:return
    raise APIException(message="unauthorised access",status_code=403)