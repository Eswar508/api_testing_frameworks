from fastapi import Depends,APIRouter
from fastapi.responses import JSONResponse
from FastApi.validations.base_models import *
from FastApi.validations.validate_request_data import *
from FastApi.utils.api_client import StudentAPIClient as S
app=APIRouter()
@app.get("/student/me",response_model=StudentResponseModel)
def get_data(token_data=Depends(verify_token)):
    student_verify(token_data)
    return S.get_account(token_data["user_id"])
@app.patch("/student/me",response_model=StudentResponseModel)
def partial_update_data(data:StudentFieldModel,token_data=Depends(verify_token)):
    student_verify(token_data)
    data=data.model_dump(exclude_unset=True)
    duplicate_identity_field_verification(data)
    return S.partial_update_account(token_data["user_id"],data)
@app.put("/student/me",response_model=StudentResponseModel)
def update_data(data:StudentModel,token_data=Depends(verify_token)):
    student_verify(token_data)
    data=data.model_dump()
    duplicate_identity_verification(data)
    return S.update_account(token_data["user_id"],data)
@app.delete("/student/me",response_model=MessageModel)
def delete_account(token_data=Depends(verify_token)):
    student_verify(token_data)
    return S.delete_account(token_data['user_id'])