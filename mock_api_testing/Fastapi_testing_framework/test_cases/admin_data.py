
from api_client.auth_client import login_client
from utils.helper_fun import *
class AdminData:
    other_admin_id=2
    def admin_token():
        data={"email":"adminA@gmail.com","password":"$AnAdmin1"}
        token=get_token(data)
        expected_data={
        "user_id":1,
        "name":"adminA",
        "email":"admin1@gmail.com",
        "age":23,
        "gender":"male",
        "department":"cse"
    }
        return [(token,expected_data)]
    def admin_ids():
        ids=[1,4]
        ex_data=[{
            "user_id":1,
            "name":"adminA",
            "email":"admin1@gmail.com",
            "age":23,
            "gender":"male",
            "department":"cse"
        }
        ,
         {
        "user_id": 4,
        "name": "adminD",
        "email": "admin4@gmail.com",
        "age": 23,
        "gender": "male",
        "department": "mechanical"
    }]
        return zip(ids,ex_data)
    patch_me={"name":"patch admin me","email":"patchedadminme@gmail.com"}
    update_me={"name":"update admin me","email":"updatedadminme@gmail.com","age":23,
        "gender":"male",
        "department":"cse"}
    update_permisssion={"name":"updating admin permitted","email":"updatedadminpermitted@gmail.com",
                        "age":23,
                        "gender":"male",
                        "department":"cse"}
    workflow_update={"name":"updated admin","email":"updatedadmin123@gmail.com",
                        "age":23,
                        "gender":"male",
                        "department":"cse"}
    patched_schema={"name":"patched schema","email":"patchedschema@gmail.com"}
    updated_schema={
        "name": "updated schema",
        "email": "updatedschema@gmail.com",
        "age": 23,
        "gender": "male",
        "department": "mechanical"
    }