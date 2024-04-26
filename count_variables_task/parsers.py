import json
import re
from pathlib import Path
from typing import Iterable

from count_variables_task.models import CodeSnippetModel, OperationResult


def get_code_snippets(path: str = "data/dirty_data.txt") -> Iterable[CodeSnippetModel]:
    dirty_data_path = Path(__file__).absolute().parents[0].joinpath(path)

    clean_regex = re.compile(r"(?<=```python\n).*?(?=```)", re.DOTALL)

    with open(dirty_data_path, "r") as dirty_data_file:
        dirty_data = dirty_data_file.read()

    for idx, match in enumerate(clean_regex.findall(dirty_data)):
        yield CodeSnippetModel(snippet_id=idx + 1, text=match.strip())


def get_results(path: str) -> list[OperationResult]:
    results_path = Path(__file__).absolute().parents[0].joinpath(path)

    with open(results_path, "r") as results_file:
        results_data = results_file.read()

    results = json.loads(results_data)

    return [OperationResult.parse_obj(result) for result in results]

def get_code_snippets_from_results(path:str = "hugging-face-data/algorithm_results.json") -> list[CodeSnippetModel]:
    results_path = Path(__file__).absolute().parents[0].joinpath(path)

    with open(results_path, "r") as results_file:
        results_data = results_file.read()

    results = json.loads(results_data)

    return [OperationResult.parse_obj(result).code_snippet for result in results]
