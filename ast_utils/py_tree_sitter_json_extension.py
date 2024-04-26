import json

from pydantic import BaseModel
from tree_sitter import Node, Tree

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
    text: str
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
