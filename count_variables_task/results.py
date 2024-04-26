import pprint

from pydantic import BaseModel

import dependencies
from ast_utils import get_by_tree_sitter, py_tree_sitter_json_extension
from count_variables_task import config, parsers, variable_counter
from count_variables_task.models import OperationResult


def get_algorithm_results() -> list[OperationResult]:
    operation_results = []

    for code_snippet in parsers.get_code_snippets():
        result = str(variable_counter.count_variable(code_snippet.text))
        operation_results.append(
            OperationResult(result=result, code_snippet=code_snippet)
        )

    return operation_results


def get_gigachat_wo_ast_results() -> list[OperationResult]:
    operation_results = []

    for code_snippet in parsers.get_code_snippets():
        result = dependencies.get_gigachat().execute(
            system_message=config.SYSTEM_MESSAGE_WO_AST,
            user_message=config.USER_MESSAGE_WO_AST.format(
                code_snippet=code_snippet.text
            ),
        )
        operation_results.append(
            OperationResult(result=result, code_snippet=code_snippet)
        )

    return operation_results


def get_gigachat_w_json_ast_results(
    start: int = 0, end: int = 100
) -> list[OperationResult]:
    operation_results = []
    code_snippets = parsers.get_code_snippets()

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
    start: int = 0, end: int = 100
) -> list[OperationResult]:
    operation_results = []
    code_snippets = parsers.get_code_snippets()

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
