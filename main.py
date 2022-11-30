from fastapi import FastAPI,Request,Depends
from BlogPosts.routers import blog
from BlogPosts.routers import user
from BlogPosts.routers import authentication
from BlogPosts.routers import password_reset
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from BlogPosts.models import BlogPost,User
from sqlalchemy.orm import Session
from BlogPosts.database import get_db

app= FastAPI(
    docs_url = "/docs",
    redoc_url= "/redocs",
    title="SIRMUSO BLOGSITE API",
    description="FRAMEWORK FOR SIRMUSO BLOGSITE API",
    version="4.0",
    openapi_url="/api/v2/openapi.json"
    
)

app.include_router(authentication.router)
app.include_router(user.router)
app.include_router(blog.router)
app.include_router(password_reset.router)

templates = Jinja2Templates(directory="BlogPosts/templates")
app.mount("/static",StaticFiles(directory="Blogposts/static"),name="static")

@app.get('/',response_class=HTMLResponse,tags=["Display"])
def home(request: Request, db:Session = Depends(get_db)):
    blogs = db.query(BlogPost).all()
    return templates.TemplateResponse("home.html",{"request":request,"blogs":blogs})

@app.get('/users',response_class=HTMLResponse,tags=["Display"])
def get_all(request: Request, db:Session = Depends(get_db)):
    users = db.query(User).all()
    return templates.TemplateResponse("users.html",{"request":request,"users":users})


