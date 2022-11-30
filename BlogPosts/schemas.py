from pydantic import BaseModel,Field
from typing import List,Optional
from datetime import datetime
from uuid import UUID, uuid4

class SchemasUser(BaseModel):
    id : int
    email: str
    username : str
    password : str
    lastname : str
    firstname : str
    created_at : datetime 

class SchemasBlog(BaseModel):
    id : UUID = Field(default_factory=uuid4)
    title: str
    content : str
    author : str
    posted_at : datetime


class UserBlog(SchemasBlog):
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    username : str
    email: str
    lastname : str
    firstname : str
    blogs : List[UserBlog]=[]
    class Config():
        orm_mode = True


class UserLogin(BaseModel):
    username : str
    password:str
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    id : int
    title: str
    content : str
    author : str
    class Config():
        orm_mode = True

class UpdateBlog(BaseModel):
    title: str
    content : str
    class Config():
        orm_mode = True

class Token(BaseModel):
    access_token : str
    token_type : str
    class Config():
        orm_mode = True
class TokenData(BaseModel):
    username:Optional[str] = None

class PasswordReset(BaseModel):
    email : str
    username :str

class NewPassword(BaseModel):
    token : str
    password : str