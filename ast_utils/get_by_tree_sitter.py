import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Tree

SEXP_AST_DESCRIPTION = """
Дерево AST представленно в формате S-выражения.
"""

PY_LANGUAGE = Language(tspython.language(), "python")

parser = Parser()
parser.set_language(PY_LANGUAGE)


def get_tree(code_snippet_text: str) -> Tree:
    return parser.parse(bytes(code_snippet_text, "utf8"))


def get_sexp(code_snippet_text: str) -> str:
    return get_tree(code_snippet_text).root_node.sexp()
