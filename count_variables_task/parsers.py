import json
import re
from pathlib import Path

from count_variables_task.models import CodeSnippetModel, OperationResult


def get_code_snippets(path: str = "data/dirty_data.txt") -> list[CodeSnippetModel]:
    dirty_data_path = Path(__file__).absolute().parents[0].joinpath(path)

    clean_regex = re.compile(r"(?<=```python\n).*?(?=```)", re.DOTALL)

    with open(dirty_data_path, "r") as dirty_data_file:
        dirty_data = dirty_data_file.read()

    return [
        CodeSnippetModel(snippet_id=idx + 1, text=match.strip())
        for idx, match in enumerate(clean_regex.findall(dirty_data))
    ]


def get_results(path: str) -> list[OperationResult]:
    results_path = Path(__file__).absolute().parents[0].joinpath(path)

    with open(results_path, "r") as results_file:
        results_data = results_file.read()

    results = json.loads(results_data)

    return [OperationResult.parse_obj(result) for result in results]
