import json
import os
import tempfile
import time
from pathlib import Path
from typing import Iterable, Optional

import lizard

import dependencies
from executors.interface import ExecutorInterface
from framework.data import parser
from framework.enums import ConditionType, ExecutorType, LanguageType
from framework.models import Case, CodeSnippet, ExecuteResult
from framework.tasks.cyclomatic_complexity import cases, messages
from framework.utils import ast

MSGS: dict[tuple[ExecutorType, ConditionType, LanguageType], tuple[str, str]] = {
    (ExecutorType.YANDEX_GPT_LITE, ConditionType.ONLY_CODE, LanguageType.PYTHON): (
        messages.SYSTEM_MSG_W_PYTHON_CODE,
        messages.USER_MSG_W_CODE,
    ),
    (ExecutorType.YANDEX_GPT_LITE, ConditionType.ONLY_CODE, LanguageType.JAVA): (
        messages.SYSTEM_MSG_W_JAVA_CODE,
        messages.USER_MSG_W_CODE,
    ),
    (ExecutorType.YANDEX_GPT_LITE, ConditionType.ONLY_SEXP_AST, LanguageType.PYTHON): (
        messages.SYSTEM_MSG_W_PYTHON_SEXP_AST,
        messages.USER_MSG_W_SEXP_AST,
    ),
    (ExecutorType.YANDEX_GPT_LITE, ConditionType.ONLY_SEXP_AST, LanguageType.JAVA): (
        messages.SYSTEM_MSG_W_JAVA_SEXP_AST,
        messages.USER_MSG_W_SEXP_AST,
    ),
    (
        ExecutorType.YANDEX_GPT_LITE,
        ConditionType.CODE_W_SEXP_AST,
        LanguageType.PYTHON,
    ): (
        messages.SYSTEM_MSG_W_PYTHON_CODE_A_SEXP_AST,
        messages.USER_MSG_W_CODE_A_SEXP_AST,
    ),
    (ExecutorType.YANDEX_GPT_LITE, ConditionType.CODE_W_SEXP_AST, LanguageType.JAVA): (
        messages.SYSTEM_MSG_W_JAVA_CODE_A_SEXP_AST,
        messages.USER_MSG_W_CODE_A_SEXP_AST,
    ),
    (ExecutorType.PHI_MINI, ConditionType.ONLY_CODE, LanguageType.PYTHON): (
        messages.SYSTEM_MSG_W_JAVA_CODE_A_SEXP_AST,
        messages.USER_MSG_W_CODE,
    ),
}

EXECUTORS: dict[ExecutorType, ExecutorInterface] = {
    ExecutorType.YANDEX_GPT_LITE: dependencies.get_yandexgpt(),
    ExecutorType.PHI_MINI: dependencies.get_phi_mini(),
}


def get_baseline_result(code_snippet: CodeSnippet) -> int:
    suffix = ast.FILE_EXTENSIONS[code_snippet.language]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        temp_file_path = temp_file.name
        temp_file.write(code_snippet.text.encode("utf-8"))

    analysis_results = lizard.analyze_file(temp_file_path)
    os.remove(temp_file_path)

    total_ccn = 0

    for func in analysis_results.function_list:
        total_ccn += func.cyclomatic_complexity

    return total_ccn


def execute_case_results(save_dir: str = "data"):
    for case in cases.get_cases():
        if case.executor not in EXECUTORS:
            continue

        if case.get_key() not in MSGS:
            continue

        executor = EXECUTORS[case.executor]
        system_msg_temp, user_msg_temp = MSGS[case.get_key()]

        execute_results: list[ExecuteResult] = []

        for code_snippet in parser.get_code_snippets(
            case.language, case.max_items, code_filter=ast.is_correct_code
        ):
            print(code_snippet.id)

            if case.ast_repr_type is not None:
                ast_repr = ast.get_ast_repr(
                    case.ast_repr_type, code_snippet.text, case.language
                )
            else:
                ast_repr = None

            system_msg = system_msg_temp.format(
                code=code_snippet.text, ast_repr=ast_repr
            )
            user_msg = user_msg_temp.format(code=code_snippet.text, ast_repr=ast_repr)

            is_available, token_cnt = executor.is_available_msg(user_msg)

            if not is_available:
                continue

            execute_result_text = executor.execute(system_msg, user_msg)
            execute_results.append(
                ExecuteResult(
                    code_snippet=code_snippet,
                    system_msg=system_msg,
                    user_msg=user_msg,
                    text=execute_result_text,
                    token_cnt=token_cnt,
                )
            )

            time.sleep(case.execute_delay)

        results_path = (
            Path(__file__).absolute().parent.joinpath(f"{save_dir}/{case}.json")
        )

        with open(results_path, "a") as results_file:
            json_results = [
                json.dumps(result.dict(), ensure_ascii=False)
                for result in execute_results
            ]
            results_file.write(f'[{",".join(json_results)}]')


def get_case_results(
    data_dir: str = "data",
) -> Iterable[tuple[Case, list[ExecuteResult]]]:
    for case in cases.get_cases():
        try:
            results_path = (
                Path(__file__).absolute().parent.joinpath(f"{data_dir}/{case}.json")
            )

            with open(results_path, "r") as results_file:
                results_data = results_file.read()

            results = json.loads(results_data)

            yield case, [ExecuteResult.parse_obj(result) for result in results]
        except FileNotFoundError as exc:
            print(f"Error in get_case_results: {exc}")
