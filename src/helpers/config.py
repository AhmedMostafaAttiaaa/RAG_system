from pydantic_settings import BaseSettings
from fastapi import Depends

class settings(BaseSettings):
    APP_NAME: str
    APP_VERSION: str
    OPEN_API_KEY: str

    FILE_ALLOWED_EXTINTIONS: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNCK_SIZE: int
    class Config:
        env_file = ".env"

def get_settings():
    return settings()
