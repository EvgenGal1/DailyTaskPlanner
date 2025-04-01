from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    PROJECT_NAME: str
    DATABASE_URL: str
    SECRET_KEY: str
    REDIS_URL: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    
    class Config:
        # опред.среду ч/з перем. ENV
        env_file = f".env.{os.getenv('ENV', 'dev')}"
        env_file_encoding = 'utf-8'

settings = Settings()