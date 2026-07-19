from fastapi import APIRouter,Depends
from FastApi.validations.base_models import *
from FastApi.validations.validate_request_data import *
from FastApi.validations.base_models import *
from FastApi.utils.api_client import StudentAPIClient as S
from FastApi.utils.api_client import AdminAPIClient as A
app=APIRouter()
@app.get("/students/{id}",response_model=StudentResponseModel)
def get_data(id:int,token_data:dict=Depends(verify_token)):
    authorize_user(token_data,id) 
    return S.get_account(id)
@app.patch("/students/{id}",response_model=StudentResponseModel)
def partial_update_data(id:int,data:StudentFieldModel,token_data:dict=Depends(verify_token)):
    authorize_user(token_data,id)
    data=data.model_dump(exclude_unset=True)
    duplicate_identity_field_verification(data)
    return S.partial_update_account(id,data)
@app.put("/students/{id}",response_model=StudentResponseModel)
def update_data(id:int,data:StudentModel,token_data:dict=Depends(verify_token)):
    authorize_user(token_data,id)
    data=data.model_dump()
    duplicate_identity_field_verification(data)
    return S.update_account(id,data)
@app.delete("/students/{id}",response_model=MessageModel)
def delete_account(id:int,token_data:dict=Depends(verify_token)):
    authorize_user(token_data,id)
    return S.delete_account(id)
@app.get("/admin/me",response_model=AdminResponseModel)
def get_data(token_data:dict=Depends(verify_token)):
    admin_verify(token_data)
    return A.get_account(token_data["user_id"])
@app.get("/admins/{id}",response_model=AdminResponseModel)
def get_admin_data(id,token_data:dict=Depends(verify_token)):
    admin_verify(token_data)
    return A.get_account(id)
@app.patch("/admin/me",response_model=AdminResponseModel)
def partial_update_admin(data:AdminFieldModel,token_data:dict=Depends(verify_token)):
    admin_verify(token_data)
    data=data.model_dump(exclude_unset=True)
    return A.partial_update_account(token_data["user_id"],data)
@app.put("/admin/me",response_model=AdminResponseModel)
def update_admin(data:AdminModel,token_data:dict=Depends(verify_token)):
    admin_verify(token_data)
    data=data.model_dump()
    duplicate_identity_field_verification(data)
    return A.update_account(token_data["user_id"],data)