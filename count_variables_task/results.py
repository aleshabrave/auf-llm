import pprint
from typing import Callable

import dependencies
from ast_utils import get_by_tree_sitter, py_tree_sitter_json_extension
from count_variables_task import config, variable_counter
from count_variables_task.models import OperationResult


def get_algorithm_results(code_snippet_getter: Callable, size: int = 100) -> list[OperationResult]:
    operation_results = []
    cnt = 0

    for code_snippet in code_snippet_getter():
        try:
            result = str(variable_counter.count_variable(code_snippet.text))
        except:
            continue

        cnt += 1
        operation_results.append(
            OperationResult(result=result, code_snippet=code_snippet)
        )

        if cnt == size:
            break

    return operation_results


def get_gigachat_wo_ast_results(code_snippet_getter: Callable, size: int = 100) -> list[OperationResult]:
    operation_results = []
    cnt = 0

    for code_snippet in code_snippet_getter():
        cnt += 1
        result = dependencies.get_gigachat().execute(
            system_message=config.SYSTEM_MESSAGE_WO_AST,
            user_message=config.USER_MESSAGE_WO_AST.format(
                code_snippet=code_snippet.text
            ),
        )
        operation_results.append(
            OperationResult(result=result, code_snippet=code_snippet)
        )

        if cnt == size:
            break

    return operation_results


def get_gigachat_w_json_ast_results(
    code_snippet_getter: Callable,
    start: int = 0, end: int = 100
) -> list[OperationResult]:
    operation_results = []
    code_snippets = code_snippet_getter()

    for i in range(start, end):
        code_snippet = code_snippets[i]
        tree = get_by_tree_sitter.get_tree(code_snippet.text)
        tree_repr = py_tree_sitter_json_extension.to_dict(tree)
        pptretty_tree_repr = pprint.pformat(tree_repr)

        user_message = config.USER_MESSAGE_W_JSON_AST.format(
            code_snippet=code_snippet.text,
            json_ast_repr=pptretty_tree_repr,
            json_ast_desctription=py_tree_sitter_json_extension.JSON_AST_DESCRIPTION,
        )
        result = dependencies.get_gigachat().execute(
            system_message=config.SYSTEM_MESSAGE_W_AST,
            user_message=user_message,
        )
        operation_results.append(
            OperationResult(result=result, code_snippet=code_snippet)
        )

    return operation_results


def get_gigachat_w_sexp_ast_results(
    code_snippet_getter: Callable,
    start: int = 0, end: int = 100
) -> list[OperationResult]:
    operation_results = []
    code_snippets = code_snippet_getter()

    for i in range(start, end):
        code_snippet = code_snippets[i]
        tree_repr = get_by_tree_sitter.get_sexp(code_snippet.text)
        pptretty_tree_repr = pprint.pformat(tree_repr)

        user_message = config.USER_MESSAGE_W_SEXP_AST.format(
            code_snippet=code_snippet.text,
            sexp_ast_repr=pptretty_tree_repr,
            sexp_ast_description=get_by_tree_sitter.SEXP_AST_DESCRIPTION,
        )
        result = dependencies.get_gigachat().execute(
            system_message=config.SYSTEM_MESSAGE_W_AST,
            user_message=user_message,
        )
        operation_results.append(
            OperationResult(result=result, code_snippet=code_snippet)
        )

    return operation_results
