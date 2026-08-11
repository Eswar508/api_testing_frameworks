from flask import Blueprint,request
from flask_api.data_base.data_services.users_service import get_user_by_email
from flask_api.helper_fun import generate_login_response
from flask_api.data_base.data_clients.helper_fun import to_dict
from flask_api.helper_fun import validate_login_schema
auth_bp=Blueprint("login",__name__)
@auth_bp.post("/login")
def login():
    login_request=request.json
    login_data,error=validate_login_schema(login_request)
    if error:
        return error,422
    response=generate_login_response(login_data)
    return response 