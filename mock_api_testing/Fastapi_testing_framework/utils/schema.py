from pydantic import BaseModel,Field
from typing import Literal,Optional
email=r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
class TokenSchema(BaseModel):
    user_id: int = Field(gt=0)
    role:Literal["student","admin"]
    iat:int
    exp:int
class CommonModel(BaseModel):
    name:str= Field(min_length=3,max_length=20,pattern=r"^[A-Za-z]+$")
    email:str=Field(pattern=email)
    gender:Literal["male","female"]
class CommonFieldModel(BaseModel):
    name:Optional[str]= Field(default=None,min_length=3,max_length=20,pattern=r"^[A-Za-z]+$")
    email:Optional[str] = Field(pattern=email,default=None)
    gender:Optional[Literal["male","female"]] = None
class StudentSchema(CommonModel):
    age:int = Field(ge=18,le=23)
    cgpa:float = Field(ge=8.0,le=10.0)
    user_id:int = Field(gt=0)
class AdminSchema(CommonModel):
    age:int = Field(ge=23,le=60)
    department:Literal['cse','ece','civil','mechanical','eee'] 
    user_id:int =Field(gt=0)
class User(BaseModel):
    user_id:int =Field(gt=0)
    name:str= Field(min_length=3,max_length=20,pattern=r"^[A-Za-z]+$")
    email:str=Field(pattern=email)
class LoginSchema(BaseModel):
    access_token:str
    token_type:Literal["Bearer"]
    user:User
class MessageSchema(BaseModel):
    message:str