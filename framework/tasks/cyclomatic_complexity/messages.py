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