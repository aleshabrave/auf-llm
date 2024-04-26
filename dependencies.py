from functools import lru_cache

from model_executors.gigachat import GigaChatExecutor
from settings import Settings


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


@lru_cache(maxsize=1)
def get_gigachat() -> GigaChatExecutor:
    return GigaChatExecutor(
        credentials=get_settings().gigachat_auth_data, verify_ssl_certs=False
    )
