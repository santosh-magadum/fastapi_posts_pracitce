
from fastapi import APIRouter,Depends,status,HTTPException,Response
from pydantic.networks import HttpUrl
from sqlalchemy.sql.expression import select

from app.database import get_db
from sqlalchemy.orm import Session
from app import schemas
from app import models
from app import util
from app import oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router=APIRouter(tags=['Authentication'])

@router.post("/login",response_model=schemas.Token)
def login(user_credential:OAuth2PasswordRequestForm = Depends() ,db: Session = Depends(get_db)):

    #print("In create login method")
    # user=select(models.User).where(models.User.email==user_credential.email)
    user=select(models.User).where(models.User.email==user_credential.username)
    user=db.execute(user).scalars().first()


    if not user:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f"Invalida credentials")

    if not util.verify(user_credential.password,user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'Invalid credentials')

    # create token

    access_token=oauth2.create_access_token(data={"user_id":user.id})
    # return token
    return {"access_token":access_token, "token_type":"bearer"}

    # return {"data":"both the passwords are matched"}
    




