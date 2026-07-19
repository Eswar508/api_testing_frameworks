from fastapi import APIRouter
from FastApi.validations.base_models import *
from FastApi.utils.api_client import StudentAPIClient as S
from FastApi.validations.validate_request_data import *
from FastApi.utils.helper_fun import generate_login_response
app=APIRouter()
@app.post("/signin",response_model=StudentResponseModel)
def register_user(data:RegisterModel):
    data=data.model_dump()
    duplicate_identity_verification(data)
    return S.save_user(data)
@app.post("/login",response_model=LoginResponseModel)
def login(data:LoginModel):
    data=data.model_dump()
    user_data=S.login_data(data)
    return generate_login_response(user_data)
