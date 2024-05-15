import json
from pathlib import Path
from typing import Callable, Iterable

from framework.enums import LanguageType
from framework.models import CodeSnippet


def get_code_snippets(
    language: LanguageType,
    total_items: int,
    path: str = "dataset.json",
    code_filter: Callable = lambda _, __: True,
) -> Iterable[CodeSnippet]:
    dataset_path = Path(__file__).absolute().parent.joinpath(path)

    with open(dataset_path, "r") as dataset_file:
        dataset = dataset_file.read()

    idx = 0
    for code in json.loads(dataset):
        if idx == total_items:
            break

        if code["language"] == language.value.lower() and code_filter(
            code["text"], language
        ):
            idx += 1

            yield CodeSnippet.parse_obj(code)
