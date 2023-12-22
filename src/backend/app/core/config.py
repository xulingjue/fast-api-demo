from typing import Optional
from pydantic import PostgresDsn


class Settings:
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = "postgresql://user:password@localhost:5432/dbname"


settings = Settings()
