from functools import lru_cache

from pydantic import BaseSettings

from app.schemas.settings import Environment


class Settings(BaseSettings):
    environment: Environment
    sql_alchemy_database_url: str = "sql:///././sql_database.db"
    api_disable_docs: bool = False
    api_debug: bool = True

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'
        use_enum_values = True


@lru_cache()
def get_settings():
    return Settings()
