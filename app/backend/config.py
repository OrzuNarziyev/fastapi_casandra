from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    cql_port: int
    cql_password: str
    cql_host: str
    cql_user: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")
