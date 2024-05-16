from pprint import pprint
from tree_sitter import Language, Parser, Tree
import tree_sitter_python as tspython
from tree_sitter import Node, Tree
from pydantic import BaseModel
import json
from framework.tasks.cyclomatic_complexity import case_results, reports

# case_results.execute_case_results()
# reports.make_total()
# reports.make_relate("yandex_gpt_lite_code_w_sexp_ast_python", "yandex_gpt_lite_only_code_python")
# reports.make_relate("yandex_gpt_lite_code_w_sexp_ast_java", "yandex_gpt_lite_only_code_java")
# reports.make_relate("phi_mini_code_w_sexp_ast_python", "phi_mini_only_code_python")

code = """
def sum(a, b):
    return a + b
"""


JSON_AST_DESCRIPTION = """
Дерево AST представленно в формате JSON, в узлах дерева есть несколько полей:
'type' – это тип узла,
'text' – это текст содержания узла,
'сhildren' – это дочерние узлы.
"""


class PointModel(BaseModel):
    row: int
    column: int


class NodeModel(BaseModel):
    type: str
    # text: str
    children: list["NodeModel"]

    def from_node(node: Node) -> "NodeModel":
        return NodeModel(
            type=node.type,
            text=node.text,
            children=[],
        )


def to_json(tree: Tree) -> str:
    root_node = tree.root_node
    root_node_model = NodeModel.from_node(root_node)

    queue = [(root_node, root_node_model)]

    while queue:
        node, node_model = queue.pop()

        for child in node.children:
            child_model = NodeModel.from_node(child)
            node_model.children.append(child_model)
            queue.append((child, child_model))

    return root_node_model.model_dump_json()


def to_dict(tree: Tree) -> dict:
    return json.loads(to_json(tree))


SEXP_AST_DESCRIPTION = """
Дерево AST представленно в формате S-выражения.
"""

PY_LANGUAGE = Language(tspython.language(), "python")

parser = Parser()
parser.set_language(PY_LANGUAGE)


def sum(a, b):
    return a + b


def get_tree(code_snippet_text: str) -> Tree:
    return parser.parse(bytes(code_snippet_text, "utf8"))


def get_sexp(code_snippet_text: str) -> str:
    return get_tree(code_snippet_text).root_node.sexp()


(
    "(module (function_definition name: (identifier) parameters: (parameters "
    "(identifier) (identifier)) body: (block (return_statement (binary_operator "
    "left: (identifier) right: (identifier))))))"
)

tree = get_sexp(code)
print(pprint(tree))
