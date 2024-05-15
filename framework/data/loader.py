import json
import re
from pathlib import Path
from typing import Iterable, Optional

from datasets import load_dataset

from framework.enums import LanguageType


def prepare_python_code(text: str) -> Optional[str]:
    clean_regex = re.compile(r"(?<=```python).*?(?=```)", re.DOTALL)
    matches = clean_regex.findall(text)

    if not matches:
        return None

    match = matches[0].strip()

    rm_single_comments_match = re.sub("(#.*?$)", "", match, flags=re.MULTILINE)

    return rm_single_comments_match.strip()


def prepare_java_code(text: str) -> Optional[str]:
    clean_regex = re.compile(r"(?<=```java).*?(?=```)", re.DOTALL)
    matches = clean_regex.findall(text)

    if not matches:
        return None

    match = matches[0].strip()

    rm_single_comments_match = re.sub("((//).*?$)", "", match, flags=re.MULTILINE)

    return rm_single_comments_match.strip()


LANGUAGES: dict[str] = {
    LanguageType.PYTHON.value.lower(): prepare_python_code,
    LanguageType.JAVA.value.lower(): prepare_java_code,
}


def _get_code_snippets(
    dataset_name: str = "nampdn-ai/tiny-codes",
) -> Iterable[tuple[str, str]]:
    dataset = load_dataset(dataset_name)

    for row in dataset["train"]:
        if row["programming_language"].lower() in LANGUAGES:
            cleaned_code = LANGUAGES[row["programming_language"].lower()](
                row["response"]
            )

            if cleaned_code is None:
                continue

            yield cleaned_code, row["programming_language"].lower()


def load(total_items: int = 10_000):
    idx = 0
    dataset_path = Path(__file__).absolute().parent.joinpath("dataset.json")
    buffer = []

    for code, language in _get_code_snippets():
        buffer.append({"id": idx, "text": code, "language": language})

        idx += 1

        if idx == total_items:
            break

    with open(dataset_path, "w") as dataset_file:
        dataset_file.write(json.dumps(buffer))
