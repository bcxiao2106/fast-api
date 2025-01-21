from pydantic_settings import BaseSettings
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):
    """Application settings."""
    APP_NAME: str = "LangChain API"
    DEBUG: bool = True
    # LLM Settings
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3.2:latest"  # default model
    # Add your API keys and other settings here
    # OPENAI_API_KEY: str
    # PINECONE_API_KEY: str
    # etc.

    class Config:
        env_file = ".env"

settings = Settings()
