from FastApi.utils.repositories import JsonRepository
from FastApi.utils.helper_fun import *
from FastApi.validations.validate_request_data import get_data_with
class APIClient:
    data_handler=JsonRepository
    @classmethod
    def get_account(cls,id):
        id=str(id)
        students=cls.data_handler.get_all()
        student=students.get(id)
        if student: return students[id]
        else:
            raise APIException(status_code=404,message= f"no users found with id : {id} found")
    @classmethod
    def update_account(cls,id,data):
        try:
            user=cls.get_account(id)
            user.update(data)
            storage=cls.data_handler.get_all()
            storage[str(id)]=user
            cls.data_handler.save_all(storage)
        except:
            raise APIException(status_code=500,message= "internal server error")
        return user
    @classmethod
    def partial_update_account(cls,id,data):
        return cls.update_account(id,data)
class StudentAPIClient(APIClient):
    @classmethod
    def login_data(cls,login_data):
        user_data=get_data_with(login_data,"email")
        if (not user_data):
            raise APIException(status_code=404,message={"message" : "email not found"})
        storage=get_data(password_path)
        id=str(user_data["user_id"])
        password=storage[id]
        if password!= login_data["password"]:
            raise APIException(status_code=401,message={"message" : "password is invalid"})
        return user_data
    @classmethod
    def save_user(cls,data):
        try:
            new_id=save_new_id()
            password=data.pop("password")
            new_user={"user_id":new_id,**data}
            save_password(password,new_id)
            storage=cls.data_handler.get_all()
            storage[str(new_id)]=new_user
            cls.data_handler.save_all(storage)
        except:
            raise APIException(status_code=500,message= "internal server error")
        return new_user
    @classmethod
    def delete_account(cls,id):
        try:
            cls.get_account(id)
            storage=cls.data_handler.get_all()
            del storage[str(id)]
            remove_id(id)
            remove_password(id)
            cls.data_handler.save_all(storage)
        except:
            raise APIException(status_code=500,message= "internal server error")
        return   {"message" : f"deleted the account with id : {id}"}
class AdminAPIClient(APIClient):
    pass