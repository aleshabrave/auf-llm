import ast

import astpretty


def count_variable(code_snippet: str) -> int:
    actual_tree = ast.parse(code_snippet)
    astpretty.pprint(actual_tree)

    variables = []
    module_variables = set()
    queue = [(None, actual_tree)]

    while queue:
        parent_sub_tree, sub_tree = queue.pop()

        for node in ast.iter_child_nodes(sub_tree):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                if parent_sub_tree is not None and isinstance(
                    parent_sub_tree, ast.FunctionDef
                ):
                    need_add = True

                    for parent_sub_tree_node in ast.iter_child_nodes(parent_sub_tree):
                        if (
                            isinstance(parent_sub_tree_node, ast.Global)
                            and node.id in parent_sub_tree_node.names
                        ):
                            need_add = False
                            break

                    if need_add:
                        variables.append(node.id)

                elif parent_sub_tree is not None and isinstance(
                    parent_sub_tree, ast.Module
                ):
                    if node.id not in module_variables:
                        variables.append(node.id)

                    module_variables.add(node.id)

                else:
                    variables.append(node.id)

            queue.append((sub_tree, node))

    return len(variables)
