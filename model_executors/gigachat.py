from dataclasses import dataclass
from typing import Any

from langchain.chat_models.gigachat import GigaChat
from langchain.schema import HumanMessage, SystemMessage


@dataclass
class GigaChatExecutor:
    _chat: GigaChat

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._chat = GigaChat(*args, **kwargs)

    def execute(self, system_message: str, user_message: str) -> str:
        messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=user_message),
        ]
        result = self._chat(messages)

        return result.content
