from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    INDEX_NAME: str
    PINECONE_API_KEY:str
    HUGGINGFACE_API_KEY:str
    GEMINI_KEY : str 

    class Config:
        env_file = ".env"
