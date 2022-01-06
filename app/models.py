
import datetime
from sqlalchemy import func
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import null, text
from sqlalchemy.sql.functions import now
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import TIMESTAMP
from app.database import Base

from sqlalchemy import Column,Integer,String,Boolean,DateTime,ForeignKey


class Posts(Base):
    __tablename__="posts"

    id = Column(Integer,primary_key=True,nullable=False)
    title=Column(String(200),nullable=False)
    content=Column(String(200),nullable=False)
    published=Column(Boolean,nullable=False,server_default=text('True'))
    # created_at=Column(TIMESTAMP(timezone=True),nullable=False,default=func.now())
    # created_at= Column(DateTime(timezone=True),nullable=False, server_default=func.now())
    owner_id=Column(Integer, ForeignKey("users.id",ondelete='CASCADE'),nullable=False)
    created_at= Column(DateTime(timezone=True),nullable=False, server_default=text('now()'))

    owner =relationship("User")




class User(Base):
    __tablename__="users"

    id = Column(Integer,primary_key=True,nullable=False)
    email=Column(String(200),nullable=False,unique=True)
    password=Column(String(500),nullable=False)
    created_at= Column(DateTime(timezone=True),nullable=False, server_default=text('now()'))
    phone_number=Column(String(10))


class Vote(Base):
    __tablename__="votes"
    post_id=Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    