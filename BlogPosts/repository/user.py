from fastapi import status,HTTPException
from sqlalchemy.orm import Session
from BlogPosts.models import User
from BlogPosts.schemas import SchemasUser
from BlogPosts.security.hashing import Hash
from BlogPosts.send_email import send_registration_mail

def create_user(request:SchemasUser,db:Session):
    new_user = User(username=request.username,email=request.email,firstname=request.firstname,
    lastname=request.lastname,password=Hash.bcrypt(request.password))

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    send_registration_mail("Successful Registration",request.email,{
        "title":f"Hey {request.username}, you have been registered successfully",
        "lastname": request.lastname,
        "firstname":request.firstname,
        "Username": request.username,
        "password":request.password
    })
    return new_user

def get_user(id:int,db:Session):
    user = db.query(User).filter(User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with id {id} not found")
    
    return user

def get_username(username:str,db:Session):
    user = db.query(User).filter(User.username==username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"User with Username {username} is not available")
    
    return user

def get_all_user(db:Session):
    users = db.query(User).all()
    return users