

from pydantic import BaseSettings
# import os



class Setting(BaseSettings):
    database_hostname:str
    # database_hostname:str
    database_port:str
    database_password:str
    database_name:str
    database_username:str
    secret_key:str
    algorithm:str
    access_token_expire_minutes:int

    class Config:
        env_file="app/.env"
        case_sensitive = False
        # env_file = os.path.expanduser('.env')

settings=Setting()

