from pydantic_settings import BaseSettings
from pydantic import Field, ConfigDict

class Settings(BaseSettings):
    openrouter_api_key: str = Field(default="")
    llm_model: str = Field(default="openai/gpt-oss-120b")
    llm_timeout: int = Field(default=60)
    max_input_chars: int = Field(default=2000)

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"  # Prevents crashes from leftover/unused variables in .env
    )

settings = Settings()