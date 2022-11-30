from fastapi import APIRouter,Depends,status,Request
from BlogPosts.schemas import ShowBlog,SchemasUser,UpdateBlog,SchemasBlog
from typing import List
from sqlalchemy.orm import Session
from BlogPosts.database import get_db
from BlogPosts.security.oauth2 import get_current_user
from BlogPosts.repository import blog
from fastapi.templating import Jinja2Templates
from BlogPosts.models import BlogPost
from fastapi.responses import HTMLResponse


router = APIRouter(
    tags=["BlogPosts"],
    prefix = "/blogs"
)
template = Jinja2Templates(directory="BlogPosts/templates")

@router.get('',response_model= List[ShowBlog],summary="Get all the Blog Posts")
def get_all(db:Session = Depends(get_db),current_user:SchemasUser = Depends(get_current_user)):
    return blog.get_all(db)

@router.post('/create', response_model=ShowBlog,status_code = status.HTTP_201_CREATED,summary="Create a Blog Posts")
def create_post(request:SchemasBlog,db:Session = Depends(get_db),current_user:SchemasUser = Depends(get_current_user)):
    return blog.create_post(request,db)

@router.delete('/delete/{id}', status_code = status.HTTP_204_NO_CONTENT,summary="Delete a Blog Posts")
def delete_post(id,db:Session = Depends(get_db),current_user:SchemasUser = Depends(get_current_user)):
    return blog.delete_post(id,db)

@router.put('/update/{id}',response_model=ShowBlog, status_code = status.HTTP_202_ACCEPTED,summary="Update a Blog Posts")
def update_post(id,request:UpdateBlog,db:Session = Depends(get_db),current_user:SchemasUser = Depends(get_current_user)):
    return blog.update_post(id,request,db)

@router.get('blogs/{id}',response_model=ShowBlog, status_code = status.HTTP_200_OK,summary="Get a Blog Posts by Id")
def show_post(id,db:Session = Depends(get_db),current_user:SchemasUser = Depends(get_current_user)):
    return blog.show_post(id,db)

@router.get('/{blog_title}',response_model=ShowBlog, status_code = status.HTTP_200_OK,summary="Get a Blog Posts by Title")
def get_title(blog_title:str,db:Session = Depends(get_db),current_user:SchemasUser = Depends(get_current_user)):
    return blog.get_title(blog_title,db)

@router.get('/{title},{author}',response_model=ShowBlog, status_code = status.HTTP_200_OK,summary="Get a Blog Posts by Title and Author")
def get_title_author(title:str,author:str,db:Session = Depends(get_db),current_user:SchemasUser = Depends(get_current_user)):
    return blog.get_title_author(title,author,db)