from dataclasses import dataclass
from typing import Any

from langchain.chat_models.gigachat import GigaChat
from langchain.schema import HumanMessage, SystemMessage

from executors.interface import ExecutorInterface


@dataclass
class GigaChatExecutor(ExecutorInterface):

    _chat: GigaChat

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        self._chat = GigaChat(*args, **kwargs)

    def execute(self, system_message: str, user_message: str) -> str:
        messages = [
            SystemMessage(content=system_message),
            HumanMessage(content=user_message),
        ]
        try:
            result = self._chat(messages)
            return result.content
        except:
            print(user_message)
            return "400 Error"
