from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    deepseek_api_key: str
    deepseek_api_url: str

    gigachat_client_secret: str
    gigachat_auth_data: str
