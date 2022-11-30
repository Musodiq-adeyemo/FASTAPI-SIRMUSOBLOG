from fastapi import APIRouter,Depends,status,UploadFile,File
from BlogPosts.schemas import ShowUser,SchemasUser
from typing import List
from sqlalchemy.orm import Session
from BlogPosts.database import get_db
from BlogPosts.security import oauth2
from BlogPosts.repository import user
from fastapi.templating import Jinja2Templates
from BlogPosts.models import User
import shutil

template = Jinja2Templates(directory="templates")


router = APIRouter(
    tags=["Users Information"],
    prefix = "/users"
)

@router.post('/create',response_model=ShowUser, status_code = status.HTTP_201_CREATED,summary="Create User Account")
def create_user(request:SchemasUser,db:Session = Depends(get_db)):
    return user.create_user(request,db)

@router.get('/{id}',response_model=ShowUser, status_code = status.HTTP_200_OK,summary="Get User by Id")
def get_user(id,db:Session = Depends(get_db),current_user:SchemasUser = Depends(oauth2.get_current_user)):
    return user.get_user(id,db)

@router.get('/get/users',response_model=List[ShowUser], status_code = status.HTTP_200_OK,summary="Get All Users")
def get_all_user(db:Session = Depends(get_db),current_user:SchemasUser = Depends(oauth2.get_current_user)):
    return user.get_all_user(db)

@router.get('/{username}',response_model=ShowUser, status_code = status.HTTP_200_OK,summary="Get User by Username")
def get_username(username:str,db:Session = Depends(get_db),current_user:SchemasUser = Depends(oauth2.get_current_user)):
    return user.get_username(username,db)

@router.post("/upload",summary="Upload your profile picture")
def upload(file:UploadFile = File(...),current_user:SchemasUser = Depends(oauth2.get_current_user)):
    with open(f"BlogPosts/static/{file.filename}","wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return f"{file.filename} has been Successfully Uploaded"