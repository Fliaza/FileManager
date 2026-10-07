from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, PostgresDsn

from os.path import abspath

class RunConfig(BaseModel):
    ip: str = "localhost"
    port: int = 8000

class ApiV1prefix(BaseModel):
     version: str = "/v1"
     users: str = "/users"

class ApiPrefix(BaseModel):
    api: str = "/api"
    api_v1: ApiV1prefix = ApiV1prefix()

class DbConfig(BaseModel):
    url: PostgresDsn
    max_overflow: int = 10,
    pool_size: int = 5
    echo: bool = False

class FilePath(BaseModel):
     files_path: str = abspath("files")

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
          env_file=".env",
          case_sensitive=False,
          env_nested_delimiter="__",
          env_prefix="APP_CONFIG__"
    )

    run: RunConfig = RunConfig()
    prefix: ApiPrefix = ApiPrefix()
    db: DbConfig
    file: FilePath = FilePath()

settings = Settings()