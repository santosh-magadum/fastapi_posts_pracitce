
from typing import Optional
from fastapi import datastructures
from pydantic import BaseModel,EmailStr
from datetime import datetime

from pydantic.types import conint
from app.models import User
from app import database
from app.database import Base


# class Post(BaseModel):
#     title:str
#     content:str
#     published:bool=True

#     #rating:Optional[int]=None


# class CreatePost(BaseModel):
#     title:str
#     content:str
#     published:bool=True

# class UpdatePost(BaseModel):
#     title:str
#     content:str
#     published:bool



## instead of all of the above class
# Here we are showing how request look like

class UserCreate(BaseModel):
    email:EmailStr
    password:str


class UserResponse(BaseModel):
    email:EmailStr
    id:int
    created_at:datetime

    class Config:
        orm_mode =True


class UserLogin(BaseModel):
    email:EmailStr
    password:str


class PostBase(BaseModel):
    title:str
    content:str
    published:bool=True
    # owner_id:int
    


class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass



## Schemas for response

class Post(PostBase):
    # we can customize the response Model here
    id:int
    created_at:datetime
    owner_id:int
    owner:UserResponse

    class Config:
        orm_mode =True





class Token(BaseModel):
    access_token:str
    token_type:str

class TokenData(BaseModel):
    id:Optional[str]=None


class Vote(BaseModel):
    post_id:int
    dir:conint(le=1)


class PostOut(BaseModel):
    Posts:Post
    votes:int

    class Config:
        orm_mode =True


    



