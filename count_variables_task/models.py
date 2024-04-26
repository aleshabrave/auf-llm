from pydantic import BaseModel


class CodeSnippetModel(BaseModel):
    snippet_id: int
    text: str


class OperationResult(BaseModel):
    result: str
    code_snippet: CodeSnippetModel
