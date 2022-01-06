
from app import schemas
from fastapi import status,Depends,HTTPException,APIRouter

from app import database
from app.database import get_db
from app import util
from app import models
from sqlalchemy.orm import Session
from app import schemas

from sqlalchemy.sql.expression import delete, select
from app import oauth2

router = APIRouter(
    prefix="/vote",
    tags=["Vote"]

)

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote:schemas.Vote,db:Session=Depends(database.get_db),current_user:int =Depends(oauth2.get_current_user)):

    ## if the post doesnot exists then return post not found 404
    query=select(models.Posts).where(models.Posts.id==vote.post_id)
    post=db.execute(query).first()

    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Post with id {vote.post_id} does not exists")


    query=select(models.Vote).where(models.Vote.post_id==vote.post_id,models.Vote.user_id==current_user.id)

    found_vote=db.execute(query).first()

    if vote.dir==1:
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f'user {current_user.id} has already voted on post {vote.post_id}')
   
        new_vote=models.Vote(post_id=vote.post_id,user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"Message":"successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{vote.post_id} for this vote doesnot exists")

        query=delete(models.Vote).where(models.Vote.post_id==vote.post_id,models.Vote.user_id==current_user.id)
        db.execute(query)
        db.commit()

        return {"message":f"successfully deleted Vote for post {vote.post_id}"}





    # if vote.dir==1:
    
