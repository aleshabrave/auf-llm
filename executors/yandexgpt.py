import time
from dataclasses import dataclass
from sqlite3 import Time
from typing import Any

import requests

from executors.interface import ExecutorInterface


@dataclass
class YandexGPTExecutor(ExecutorInterface):

    model_uri: str
    headers: dict[str, str]

    def __init__(self, folder_id: str, iam_token: str) -> None:
        self.model_uri = f"gpt://{folder_id}/yandexgpt-lite/latest"
        self.headers = {"Authorization": f"Bearer {iam_token}"}

    def get_token_cnt(self, text: str) -> None:
        url = "https://llm.api.cloud.yandex.net/foundationModels/v1/tokenize"
        body = {"modelUri": self.model_uri, "text": text}
        response = requests.post(
            url=url, json=body, headers=self.headers, timeout=5
        ).json()

        return len(response["tokens"])

    def execute(self, system_message: str, user_message: str) -> str:
        url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completionAsync"
        body = {
            "modelUri": self.model_uri,
            "completionOptions": {
                "stream": True,
                "temperature": 0,
                "maxTokens": 20,
            },
            "messages": [
                {"role": "system", "text": system_message},
                {"role": "user", "text": user_message},
            ],
        }

        response = requests.post(url=url, json=body, headers=self.headers).json()
        operation_result = self._get_operation_result(response["id"])

        return operation_result

    def is_available_msg(
        self, text: str, max_token_cnt: int = 1500
    ) -> tuple[bool, int]:
        token_cnt = self.get_token_cnt(text)

        return token_cnt < max_token_cnt, token_cnt

    def _get_operation_result(self, operation_id: str) -> str:
        url = f"https://operation.api.cloud.yandex.net/operations/{operation_id}"

        while True:
            try:
                response = requests.get(url=url, headers=self.headers, timeout=5).json()
                print(response)

                if response["done"]:
                    return response["response"]["alternatives"][0]["message"]["text"]

                time.sleep(1)
            except Exception as exc:
                print(f"Error for {operation_id=}: {exc}")
