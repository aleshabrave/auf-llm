from abc import abstractmethod
from typing import Protocol


class ExecutorInterface(Protocol):

    @abstractmethod
    def execute(self, system_msg: str, user_msg: str) -> str:
        pass

    @abstractmethod
    def get_token_cnt(self, text: str) -> None:
        pass

    @abstractmethod
    def is_available_msg(self, text: str, max_token_cnt) -> tuple[bool, int]:
        pass
