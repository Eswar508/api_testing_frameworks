import jwt
import datetime
from flask import request,g
from flask_api.data_base.data_services.product_services import *
from flask_api.data_base.data_services.users_service import *
from flask_api.schema_validation import *
from marshmallow import ValidationError
from config import SECRET_KEY,ALGORITHM,JWT_EXPIRY_HOURS
from functools import wraps
def allowed_for_only_admins(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        if g.user["role"] != "admin":
            return {"message":"Forbidden"},403
        return func(*args,**kwargs)
    return wrapper
def generate_token(role,id):
        payload={
        "user_id":id,
        "iat":datetime.datetime.now(datetime.timezone.utc),
        "exp":datetime.datetime.now(datetime.timezone.utc)+datetime.timedelta(hours=JWT_EXPIRY_HOURS),
        "role":role
        }
        SECRETKEY=SECRET_KEY
        ALG=ALGORITHM
        Token=jwt.encode(payload,SECRETKEY,algorithm=ALG)
        return Token
def generate_login_response(data):
    user=get_user_by_email(data["email"])
    if user is None:return {"message":"Unauthorised"},401
    role="admin" if user.role=="admin" else "staff"
    id=user.user_id
    Token=generate_token(role,id)
    response={
        "access_token":Token,
        "token_type":"Bearer",
        "user":{
            "user_id":id,
            "name":user.name,
            "email":user.email
        }
    }
    return response
def token_data(token):
    SECRETKEY=SECRET_KEY
    ALG=ALGORITHM
    try:
        payload = jwt.decode(
            token,
            SECRETKEY,
            algorithms=[ALG]
        )
        return payload
    except:return None
def verify_token():
    try:
        schema,token=request.headers.get("Authorization").split()
    except:
        return None
    if schema != "Bearer":
        return None
    return token
def verify_user_presence(token_data):
    id=token_data["user_id"]
    role=token_data["role"]
    user=get_user(user_id=id,role=role)
    try:return user_dict(user)
    except:return None
def validate_product_schema(product):
    schema=ProductSchema()
    try:
        validated_data=schema.load(product)
        return validated_data,None
    except ValidationError as err:
        return None,{"message":err.messages}
def validate_token_schema(token_data):
    schema=token_data_schema()
    try:
        validate_data=schema.load(token_data)
        return validate_data,None
    except ValidationError as err:
        return None,{"message":err.messages}
def validate_patch_schema(product):
    schema=ProductSchema()
    try:
        validated_data=schema.load(product,partial=True)
        return validated_data,None
    except ValidationError as err:
        return None,{"message":err.messages}
def validate_login_schema(login_data):
    schema=LoginSchema()
    try:
        validated_data=schema.load(login_data)
        return validated_data,None
    except ValidationError as err:
        return None,{"message":err.messages}