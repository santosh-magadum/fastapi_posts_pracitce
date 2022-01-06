




from typing import Optional,List
from fastapi import Response,status,HTTPException,Depends,APIRouter
from fastapi.security import oauth2



from app import util

from sqlalchemy.sql.expression import delete, select, update
from starlette.status import HTTP_201_CREATED
#import mysql-0.0.3.dist-info

from app import oauth2

# from . import models
from app import models
# from app import models
from app.database import engine,get_db
from sqlalchemy.orm import Session, query
from app import schemas
from app import oauth2
from sqlalchemy import func


router =APIRouter(
    prefix="/posts",
    tags=['Posts']
)


# bydefault request comes with Get Method and url:'/'


@router.get("/sqlalchemy")
def test_posts(db: Session = Depends(get_db)):

# statement = select(Student)

# result = session.execute(statement).scalars().all()
    statement=select(models.Posts)
    print(statement)
    result=db.execute(statement).scalars().all()
    print(result)
    return result

    # result = session.execute(statement).scalars().all()




# @router.get('/',response_model=List[schemas.Post])
@router.get('/',response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user),limit: int=10,skip:int=0,
search:Optional[str]=""):
# response_model=schemas.Post
    # statement=select(models.Posts).where(models.Posts.title.contains(search)).limit(limit).offset(skip)
    # statement=select(models.Posts)
    # result=db.execute(statement).scalars().all()
    query=select(models.Posts,func.count(models.Vote.post_id).label("votes")).join(
        models.Vote,models.Vote.post_id==models.Posts.id,isouter=True).group_by(models.Posts.id).where(
            models.Posts.title.contains(search)).limit(limit).offset(skip)
    # query=select(models.Posts.owner_id,models.Posts.title)
    
    post=db.execute(query).all()
    # .all()
    # print("result")
    # print(temp[0].__dict__.items())
    # print("Votes value",temp[0].__dict__.get('votes'))
    print(post)

    return post
    # return result

    query=select(models.Posts,func.count(models.Vote.post_id).label("votes")).join(models.Vote,models.Vote.post_id==models.Posts.id,isouter=True).group_by(models.Posts.id)
    # all_posts=connect_db("SELECT * FROM posts")
    # return {'data':all_posts}


# schema for create _posts
# title:str ,content:str 


# @app.post("/posts",status_code=HTTP_201_CREATED)
# def create_posts(post: Post):
#     #print(post)
#     q=""" insert into posts (titile,content,published) values (%s,%s,%s) """
#     val=(post.title,post.content,post.published)
#     result=connect_db(q,'insert',val)
#     print(result)
#     inp=post.dict()
#     inp.update({'id':result})
#     # post_dict=post.dict()
#     # post_dict['id']=randrange(0,1000000)
#     # my_posts.append(post_dict)
#     return {'data':inp}

@router.get("/current_user_posts/{id}",response_model=List[schemas.Post])
def get_current_user_post(id:int ,db: Session = Depends(get_db), current_user:int=Depends(oauth2.get_current_user)):

    if id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'Not Authorised to perform requested action')

    statement=select(models.Posts).where(models.Posts.owner_id==id)

    result=db.execute(statement).scalars().all()
    return result

@router.post("/",status_code=HTTP_201_CREATED,response_model=schemas.Post)
def create_posts(post: schemas.PostCreate,db: Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):

    # create the new post using the sqlalchemy

    # result=models.Posts(title=post.title,content=post.content,published=post.published)

    
    result=models.Posts(owner_id=current_user.id,**post.dict())
    db.add(result)
    db.commit()
    db.refresh(result)
    return result




# @app.get('/posts/latest')
# def get_latest_post():
#     return {'Latest post detail ':my_posts[-1]}

@router.get('/{id}',response_model=schemas.PostOut)
def get_post(id: int,response:Response,db: Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):

    # statement=select(models.Posts).where(models.Posts.id==id)
    statement=select(models.Posts,func.count(models.Vote.post_id).label("votes")).join(
        models.Vote,models.Vote.post_id==models.Posts.id,isouter=True).group_by(models.Posts.id)
    result=db.execute(statement).first()

    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id :{id} details are not found")
    return result


    # print(id)

    # post_by_id=connect_db("SELECT * FROM posts where id= '%s'",value=(id,))
    # if not post_by_id:
    #     return {'data':f'the data is not found with id :{id}'}
    # return {'data':post_by_id}



    # for each_dict in my_posts:
    #     if each_dict['id']==id:
    #         return {'post_detail_is':each_dict}
    # #response.status_code=status.HTTP_404_NOT_FOUND
    # #return {'post_detail':f"id :{id} details are not found"}
    # raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id :{id} details are not found")


@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int,db: Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):

    

    
    query=select(models.Posts).where(models.Posts.id==id)
    post=db.execute(query).scalars().first()
    print("Post value from db")

    print(post)

    if post is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Post with id {id} does not exists')

    if post.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'Not Authorised to perform requested action')

    statement=delete(models.Posts).where(models.Posts.id==id)
    # post.delete(synchronize_session=False)
    db.execute(statement)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


    
    


    # post_by_id=connect_db("DELETE FROM posts where id= '%s'",'delete',value=(id,))
    # if not post_by_id:
    #     return {'data':f'the data is not found with id :{id}'}
    # return {'data':post_by_id+f" with id:{id}"}
    # for index in range(len(my_posts)):
    #     if my_posts[index]['id']==id:
    #         #temp_list=my_posts[:index]+my_posts[index+1]
    #         #return 
    #         break
    # else:
    #     return Response(status_code=status.HTTP_404_NOT_FOUND)
    #     #{"detail":f'specified id:{id} is not found'}
    # my_posts.pop(index)
    # return {'message':f'following id:{id} is deleted from the db'}


@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int,post: schemas.PostCreate,db: Session = Depends(get_db),current_user:int = Depends(oauth2.get_current_user)):

    statement=select(models.Posts).where(models.Posts.id==id)
    result=db.execute(statement).scalars().first()


    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"id :{id} details are not found")
    
    if result.owner_id!=current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'Not Authorised to perform requested action')

    query=update(models.Posts).where(models.Posts.id==id).values(**post.dict()).execution_options(synchronize_session='fetch')

    f_result=db.execute(query)
    print(f_result)
    db.commit()
    return result
    #str(f_result.rowcount)+' No of rows affected'

    # query=''' update posts set title =%s ,content = %s , published =%s where id = %s '''
    # , content ='%s', published ='%s'
    # sql = "UPDATE posts SET title = 'my name is santy' WHERE id = 7"
    # query="update posts set "
    # val_list=[]
    # print(post)
    # for key,value in post.dict().items():
    #     if value!=None:
    #         query+="'%s'='%s',"
    #         val_list.append(key)
    #         val_list.append(value)
    # else:
    #     query=query[:-1]+" where '%s'=%s ;"
    #     val_list.append('id')
    #     val_list.append(str(id))
    #     #val_list.append(',')

    # print(query)
    # print(val_list)

    # post_by_id=connect_db(query,'update',value=(post.title,post.content,post.published,id))
    # post.content,post.published
    #post_by_id=connect_db(query,'update')
    # return (f'id: {id} values are updated successfully')
    # print(post_by_id)
    # return ({'data':post_by_id})




    # for t_post in my_posts:
    #     if t_post['id']==id:
    #         for key,value in post.dict().items():
    #             t_post[key]=value
    #         break
    # else:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'id: {id} is not found')
    #     #f'id {id} is not present in the db'
    # return (f'id: {id} values are updated successfully')