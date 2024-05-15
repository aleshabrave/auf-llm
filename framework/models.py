from typing import Optional

from pydantic import BaseModel

from framework.enums import AstReprType, ConditionType, ExecutorType, LanguageType


class CodeSnippet(BaseModel):
    language: LanguageType
    text: str
    id: int


class ExecuteResult(BaseModel):
    code_snippet: CodeSnippet
    system_msg: str
    user_msg: str
    text: str
    token_cnt: int


class Case(BaseModel):
    executor: ExecutorType
    condition: ConditionType
    language: LanguageType
    max_items: int
    ast_repr_type: Optional[AstReprType]
    execute_delay: float

    def __str__(self) -> str:
        return f"{self.executor.value}_{self.condition.value}_{self.language.value}"

    def get_key(self) -> tuple[str, str, str]:
        return self.executor.value, self.condition.value, self.language.value


class AssertResult(BaseModel):
    name: str
    clean_total: int
    total: int
    mistakes: int
    accuracy: float
    mae: float
    eps_1_accuracy: float
    eps_2_accuracy: float
    eps_3_accuracy: float
