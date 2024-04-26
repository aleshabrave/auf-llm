import re
from typing import Iterable
from datasets import load_dataset
from count_variables_task.models import CodeSnippetModel


def get_code_snippets(dataset_name: str = "nampdn-ai/tiny-codes") -> Iterable[CodeSnippetModel]:
    dataset = load_dataset(dataset_name)
    clean_regex = re.compile(r"(?<=```python).*?(?=```)", re.DOTALL)

    for idx, row in enumerate(dataset['train']):
        if row['programming_language'] != 'Python':
            continue

        if row['adjective'] not in ['Low']:
            continue

        matches = clean_regex.findall(row['response'])

        if not matches:
            continue
            
        match = clean_regex.findall(row['response'])[0].strip()

        yield CodeSnippetModel(snippet_id=idx + 1, text=match)
