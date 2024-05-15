import os
import tempfile
from typing import Optional

import lizard
from tree_sitter import Tree
from tree_sitter_languages import get_parser

from framework.enums import AstReprType, LanguageType

FILE_EXTENSIONS: dict[str, str] = {
    LanguageType.PYTHON: ".py",
    LanguageType.JAVA: ".java",
}
python_parser = get_parser("python")
java_parser = get_parser("java")


def _get_tree(code_snippet_text: str, language: LanguageType) -> Tree:
    if language == LanguageType.JAVA:
        parser = java_parser
    elif language == LanguageType.PYTHON:
        parser = python_parser

    return parser.parse(bytes(code_snippet_text, "utf8"))


def _get_sexp(code_snippet_text: str, language: LanguageType) -> str:
    return _get_tree(code_snippet_text, language).root_node.sexp()


def get_ast_repr(
    ast_repr_type: AstReprType, text: str, language: LanguageType
) -> Optional[str]:
    if ast_repr_type == AstReprType.SEXP:
        return _get_sexp(text, language)


def is_correct_code(code: str, language: LanguageType) -> bool:
    suffix = FILE_EXTENSIONS[language]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
        temp_file_path = temp_file.name
        temp_file.write(code.encode("utf-8"))

    analysis_results = lizard.analyze_file(temp_file_path)
    os.remove(temp_file_path)

    if not analysis_results.function_list:
        return False

    return True
