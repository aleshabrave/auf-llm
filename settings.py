from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    gigachat_client_secret: str
    gigachat_auth_data: str

    yandex_gpt_folder_id: str
    yandex_gpt_iam_token: str
