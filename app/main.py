#from __future__ import absolute_import

import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from os import stat
from fastapi import FastAPI,Response,status,HTTPException,Depends

from random import randrange


from starlette.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND
#import mysql-0.0.3.dist-info


# from . import models
# import models
from app import models
# from app import models

from app.database import engine,get_db

from app import schemas

from app.routers import post,user,auth,vote
# from config import settings
from fastapi.middleware.cors import CORSMiddleware




# models.Base.metadata.create_all(bind=engine) # After adding the alembic this is not required because by usign the autogenerate alembic
# command we are creating the revision point from there it is very easy to create all the tables into db

app=FastAPI()

origins=["https://www.google.com",]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)




@app.get("/")
async def root():
    return {'message':'Welcome to my api'}








## code to update data to db using mysql.connector

# def connect_db(query,method='select',value=None):
#     # mydb = mysql.connector.connect(
#     # host="localhost",
#     # user="root",
#     # password="Welcome@1"
#     # )
    
#     mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Welcome@1",
#     database="fastapi"
#     )

#     mycursor = mydb.cursor(dictionary=True)
#     if method=='select':

#         print("inside the select method")

#         mycursor.execute(query,value)
        

#         myresult = mycursor.fetchall()
#         # myresult = mycursor.fetchone()
#         #print("select statement result",myresult)
#         return myresult

#     if method=='insert':
#         mycursor.execute(query,value)
#         myresult = mycursor.fetchone()
#         mydb.commit()
#         r=mycursor.lastrowid
#         print('insert query is executed')
#         return r

#     if method=="delete":
#         mycursor.execute(query,value)
#         #myresult = mycursor.fetchone()
#         mydb.commit()
#         #r=mycursor.lastrowid
#         print('delete query is executed')
#         return 'Row is deleted successfully'

#     if method=="update":
#         print(query)
#         print(value)
#         mycursor.execute(query,value)
#         #myresult = mycursor.fetchone()
#         mydb.commit()
#         #r=mycursor.lastrowid
#         print('updated query is executed')
#         return 'Row is updated successfully'

    #for x in myresult:
        #print(x)



## temperarily storing the data
# my_posts=[{"title":"title of post 1","content":"content of post 1","id":1},{"title":"favorite foods","id":2,"content":"I like dosa"}]

# while True:
#     try:
#         connect_db("SELECT * FROM posts")
#         print("connected to the mysql server and all the data's are fetched")
#         break
#     except Exception as e:
#         print("inside the exception")
#         print(e)
#         time.sleep(2)
    










    

