#  system messages

SYSTEM_MSG_W_PYTHON_CODE = "Ты вычисляешь цикломатическую сложность для фрагмента Python кода, выводи только одно чиcло цикломатической сложности без комментариев и без объяснений."
SYSTEM_MSG_W_JAVA_CODE = "Ты вычисляешь цикломатическую сложность для фрагмента Java кода, выводи только одно чиcло цикломатической сложности без комментариев и без объяснений."

SYSTEM_MSG_W_PYTHON_CODE_A_SEXP_AST = """
Ты вычисляешь цикломатическую сложность для фрагмента Python кода.
После первой пары символов "--" будет начинаться код, после второй пары "--" код будет заканчиваться.
Также будет передано представление AST дерева для кода.
После первой пары символов "**" будет начинаться представление AST дерева, после второй пары "**" представление AST дерева будет заканчиваться.
        
Выводи только одно число цикломатической сложности без комментариев и без объяснений.
"""

SYSTEM_MSG_W_JAVA_CODE_A_SEXP_AST = """
Ты вычисляешь цикломатическую сложность для фрагмента Java кода.
После первой пары символов "--" будет начинаться код, после второй пары "--" код будет заканчиваться.
Также будет передано представление AST дерева для кода.
После первой пары символов "**" будет начинаться представление AST дерева, после второй пары "**" представление AST дерева будет заканчиваться.
        
Выводи только одно число цикломатической сложности без комментариев и без объяснений.
"""

SYSTEM_MSG_W_PYTHON_SEXP_AST = """
Ты вычисляешь цикломатическую сложность Python кода, используя представление AST для кода.
Дерево AST будет представленно в формате S-выражения.
Выводи только одно число цикломатической сложности без комментариев и без объяснений.
"""

SYSTEM_MSG_W_JAVA_SEXP_AST = """
Ты вычисляешь цикломатическую сложность Java кода, используя представление AST для кода.
Дерево AST будет представленно в формате S-выражения.
Выводи только одно число цикломатической сложности без комментариев и без объяснений.
"""

SYSTEM_MSG_FSP_W_PYTHON_CODE = [
    """
Can you calculate cyclomatic complexity for Python code and write only number?
After the first pair of ‘--’ characters the code will start, after the second pair of ‘--’ characters the code will end.

--
def array_sum(array):
    total = 0
    for item in array:
        total += item
    
    return total
--
""",
    """2""",
]

SYSTEM_MSG_FSP_W_JAVA_CODE = [
    """
Can you calculate cyclomatic complexity for Java code and write only number?
After the first pair of ‘--’ characters the code will start, after the second pair of ‘--’ characters the code will end.

--
class HelloWorld {
    public static int main(String[] args) {
        for (var i = 0; i < 1; i ++) {
            var k = 0;
        }
        return 1337;
    }
}
--
""",
    """2""",
]

SYSTEM_MSG_FSP_W_PYTHON_SEXP_AST = [
    """
Can you calculate cyclomatic complexity for Python code using only AST representation for code and write only number?
After the first pair of ‘**’ characters the AST representation will start, after the second pair of ‘**’ characters the AST representation will end.
The AST tree represented in S-expression format.

**
(module (function_definition name: (identifier) parameters: (parameters (identifier)) body: (block (expression_statement (assignment left: (identifier) right: (integer))) (for_statement left: (identifier) right: (identifier) body: (block (expression_statement (augmented_assignment left: (identifier) right: (identifier))))) (return_statement (identifier)))))
**
""",
    """2""",
]

SYSTEM_MSG_FSP_W_JAVA_SEXP_AST = [
    """
Can you calculate cyclomatic complexity for Java code using only AST representation for code and write only number?
After the first pair of ‘**’ characters the AST representation will start, after the second pair of ‘**’ characters the AST representation will end.
The AST tree represented in S-expression format.

**
(program (class_declaration name: (identifier) body: (class_body (method_declaration (modifiers) type: (integral_type) name: (identifier) parameters: (formal_parameters (formal_parameter type: (array_type element: (type_identifier) dimensions: (dimensions)) name: (identifier))) body: (block (for_statement init: (local_variable_declaration type: (type_identifier) declarator: (variable_declarator name: (identifier) value: (decimal_integer_literal))) condition: (binary_expression left: (identifier) right: (decimal_integer_literal)) update: (update_expression (identifier)) body: (block (local_variable_declaration type: (type_identifier) declarator: (variable_declarator name: (identifier) value: (decimal_integer_literal))))) (return_statement (decimal_integer_literal)))))))
**
""",
    """2""",
]

SYSTEM_MSG_FSP_W_PYTHON_CODE_A_SEXP_AST = [
    """
Can you calculate cyclomatic complexity for Python code using AST representation for code and write only number?
After the first pair of ‘--’ characters the code will start, after the second pair of ‘--’ characters the code will end.
After the first pair of ‘**’ characters the AST representation will start, after the second pair of ‘**’ characters the AST representation will end.
The AST tree represented in S-expression format.

--
def array_sum(array):
    total = 0
    for item in array:
        total += item
    
    return total
--

**
(module (function_definition name: (identifier) parameters: (parameters (identifier)) body: (block (expression_statement (assignment left: (identifier) right: (integer))) (for_statement left: (identifier) right: (identifier) body: (block (expression_statement (augmented_assignment left: (identifier) right: (identifier))))) (return_statement (identifier)))))
**
""",
    """2""",
]

SYSTEM_MSG_FSP_W_JAVA_CODE_A_SEXP_AST = [
    """
Can you calculate cyclomatic complexity for Java code using AST representation for code and write only number?
After the first pair of ‘--’ characters the code will start, after the second pair of ‘--’ characters the code will end.
After the first pair of ‘**’ characters the AST representation will start, after the second pair of ‘**’ characters the AST representation will end.
The AST tree represented in S-expression format.

--
class HelloWorld {
    public static int main(String[] args) {
        for (var i = 0; i < 1; i ++) {
            var k = 0;
        }
        return 1337;
    }
}
--

**
(program (class_declaration name: (identifier) body: (class_body (method_declaration (modifiers) type: (integral_type) name: (identifier) parameters: (formal_parameters (formal_parameter type: (array_type element: (type_identifier) dimensions: (dimensions)) name: (identifier))) body: (block (for_statement init: (local_variable_declaration type: (type_identifier) declarator: (variable_declarator name: (identifier) value: (decimal_integer_literal))) condition: (binary_expression left: (identifier) right: (decimal_integer_literal)) update: (update_expression (identifier)) body: (block (local_variable_declaration type: (type_identifier) declarator: (variable_declarator name: (identifier) value: (decimal_integer_literal))))) (return_statement (decimal_integer_literal)))))))
**
""",
    """2""",
]

# user messages

USER_MSG_W_CODE = """
{code}
"""

USER_MSG_W_CODE_A_SEXP_AST = """
Информация из представления AST может помочь в вычислении цикломатической сложности.
Дерево AST представленно в формате S-выражения.

**
{ast_repr}
**

--
{code}
--
"""

USER_MSG_W_SEXP_AST = """
{ast_repr}
"""

USER_MSG_FSP_W_CODE = """
--
{code}
--
"""

USER_MSG_FSP_W_SEXP_AST = """
**
{ast_repr}
**
"""

USER_MSG_FSP_W_CODE_A_SEXP_AST = """
--
{code}
--

**
{ast_repr}
**
"""
