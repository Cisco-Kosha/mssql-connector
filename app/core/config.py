import os
import secrets
import urllib
from logging.config import dictConfig
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator
from app.utils.logging import LogConfig
import logging
import pyodbc

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    PROJECT_NAME: str = "mssql-connector"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    DB_USER: str = None
    DB_PASSWORD: str = None
    DB_SERVER: str = None
    DB_NAME: str = None
    DB_PORT: str = None

    SQLALCHEMY_DATABASE_URI: str = None

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return 'mssql+pyodbc://{0}:{1}@{2}:{3}/{4}?driver=ODBC+Driver+17+for+SQL+Server?trusted_connection=yes'.format(
            os.getenv('DB_USER'), os.getenv('DB_PASSWORD'),
            os.getenv('DB_SERVER'), os.getenv('DB_PORT', '1433'), os.getenv('DB_NAME'))

    class Config:
        case_sensitive = True


settings = Settings()

dictConfig(LogConfig().dict())
logger = logging.getLogger(settings.PROJECT_NAME)