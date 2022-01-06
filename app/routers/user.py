

from starlette.routing import Router
from app import schemas
from fastapi import status,Depends,HTTPException,APIRouter

from app import database
from app.database import get_db
from app import util
from app import models
from sqlalchemy.orm import Session

from sqlalchemy.sql.expression import select

router = APIRouter(
    prefix="/users",
    tags=["Users"]

)

# Dealing with the User
## when we are going to create something always status code has to be 201
@router.post("/",status_code=status.HTTP_201_CREATED,response_model=schemas.UserResponse)
def create_user(user:schemas.UserCreate,db: Session = Depends(get_db)):

    

    ## hash the password -user.password
    hashed_password=util.hash(user.password)
    user.password=hashed_password

    new_user=models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get('/{id}',response_model=schemas.UserResponse)
def get_user(id: int,db: Session = Depends(get_db)):
    query=select(models.User).where(models.User.id==id)
    user=db.execute(query).scalars().first()

    # statement=select(models.Posts).where(models.Posts.id==id)
    # result=db.execute(statement).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with id: {id} does not exist')
    print(user)
    return user
