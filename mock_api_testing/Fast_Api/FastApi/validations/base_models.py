from pydantic import BaseModel,Field, field_validator
import re
from FastApi.utils.helper_fun import APIException
from typing import Literal,Optional
email=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
class TokenModel(BaseModel):
    user_id: int = Field(gt=0)
    role:Literal["student","admin"]
    iat:int
    exp:int
class CommonModel(BaseModel):
    name:str= Field(min_length=3,max_length=20,pattern=r"^[A-Za-z ]+$")
    email:str=Field(pattern=email)
    gender:Literal["male","female"]
class CommonFieldModel(BaseModel):
    name:Optional[str]= Field(default=None,min_length=3,max_length=20,pattern=r"^[A-Za-z ]+$")
    email:Optional[str] = Field(pattern=email,default=None)
    gender:Optional[Literal["male","female"]] = None
class StudentModel(CommonModel):
    age:int = Field(ge=18,le=23)
    cgpa:float = Field(ge=7.5,le=10.0)
class PasswordModel(BaseModel):
    password: str
    @field_validator("password")
    @classmethod
    def validate_password(cls, value):
        error=[]
        if len(value) <8:
            error.append("more than 8 charecteres")
        if len(value) >15:
            error.append("less than 15 charecters")
        if not re.search(r"[a-z]", value):
            error.append(" a lowercase letter")
        if not re.search(r"[A-Z]", value):
            error.append("an uppercase letter")
        if not re.search(r"\d", value):
            error.append("a digit")
        if not re.search(r"[@$!%*?&]", value):
            error.append("a special character")
        if error:
            raise APIException(status_code=422,message=f"password must contain {",".join(error)}")
        return value
class RegisterModel(StudentModel,PasswordModel):
    pass
class StudentResponseModel(StudentModel):
    user_id:int = Field(gt=0)
class StudentFieldModel(CommonFieldModel):
    age:Optional [int] = Field(default=None,ge=18,le=23)
    cgpa:Optional [float] = Field(default=None,ge=7.5,le=10.0)  
class AdminModel(CommonModel):
    age:int = Field(ge=23,le=60)
    department:Literal['cse','ece','civil','mechanical','eee'] 
class AdminFieldModel(CommonFieldModel):
    age:Optional[int] = Field(default=None,ge=23,le=60)
    department:Optional[Literal['cse','ece','civil','mechanical','eee']] = None  
class AdminResponseModel(AdminModel):
    user_id:int =Field(gt=0)
class LoginModel(BaseModel):
    email:str=Field(pattern=email)
    password:str
class User(BaseModel):
    user_id:int =Field(gt=0)
    name:str= Field(min_length=3,max_length=20,pattern=r"^[A-Za-z ]+$")
    email:str=Field(pattern=email)
class LoginResponseModel(BaseModel):
    access_token:str
    token_type:Literal["Bearer"]
    user:User
class MessageModel(BaseModel):
    message:str