from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import sessionmaker
# import config
from .config import settings


# SQLALCHEMY_DATABASE_URL = 'mysql://root:santosh&123@localhost/fastapi'
SQLALCHEMY_DATABASE_URL = f"""mysql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"""
# mysql://root:santosh&123@localhost:5432/root

# print("sql alchemy database url",SQLALCHEMY_DATABASE_URL)
# "jdbc:mysql://localhost:3306/fastapi"
# 'mysql://username:password@localhost/db_name'
# 'mysql://localhost:Welcome@1@localhost/fastapi'

#  "sqlite:///./sql_app.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
