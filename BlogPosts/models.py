from sqlalchemy import Integer,Column,String,DateTime,ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import func
from BlogPosts.database import Base,engine




class User(Base):
    __tablename__= "user"
    id = Column(Integer(), primary_key=True)
    email = Column(String(200), unique=True)
    username = Column(String(100),unique=True)
    password =Column(String(20))
    firstname = Column(String(100),nullable=False)
    lastname = Column(String(100),nullable=False)
    created_at =Column(DateTime(timezone=True), server_default = func.now())
    blogs= relationship('BlogPost',back_populates = "creator")

    def __repr__(self):
        return f"User {self.username}"

class BlogPost(Base):
    __tablename__= "blogposts"
    id = Column(Integer(), primary_key=True)
    title = Column(String(100),nullable=False)
    content = Column(String(1000),nullable=False)
    author = Column(String(20),nullable=False)
    posted_at = Column(DateTime(timezone=True), server_default = func.now())
    poster_id = Column(Integer())
    user_id = Column(Integer, ForeignKey('user.id'))
    creator = relationship('User',back_populates="blogs")

    def __repr__(self):
        return f"User {self.title} and BY:{self.author}"

Base.metadata.create_all(bind=engine)