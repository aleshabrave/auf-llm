from functools import lru_cache

from executors.gigachat import GigaChatExecutor
from executors.phi_mini import PhiMiniExecutor
from executors.yandexgpt import YandexGPTExecutor
from settings import Settings


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()


@lru_cache(maxsize=1)
def get_gigachat() -> GigaChatExecutor:
    return GigaChatExecutor(
        credentials=get_settings().gigachat_auth_data, verify_ssl_certs=False
    )


@lru_cache(maxsize=1)
def get_yandexgpt() -> YandexGPTExecutor:
    return YandexGPTExecutor(
        folder_id=get_settings().yandex_gpt_folder_id,
        iam_token=get_settings().yandex_gpt_iam_token,
    )


@lru_cache(maxsize=1)
def get_phi_mini() -> PhiMiniExecutor:
    return PhiMiniExecutor()
