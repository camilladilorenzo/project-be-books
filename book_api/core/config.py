from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "BOOK REVIEW SERVICE"
    PROJECT_VERSION: str = "1.0.0"
    HOST: str = "0.0.0.0"
    PORT: int = 80
    DB_HOST: str 
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_DATABASE: str


    class Config:
        env_file = ".env"

settings = Settings()
