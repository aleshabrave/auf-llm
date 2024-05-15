from enum import Enum


class ExecutorType(str, Enum):
    GIGACHAT_LITE = "gigachat_live"
    YANDEX_GPT_LITE = "yandex_gpt_lite"
    PHI_MINI = "phi_mini"
    LLAMA_7b = "llama_7b"
    CODE_LLAMA_7b = "code_llama_7b"


class ConditionType(str, Enum):
    ONLY_CODE = "only_code"
    ONLY_SEXP_AST = "only_sexp_ast"
    CODE_W_SEXP_AST = "code_w_sexp_ast"


class LanguageType(str, Enum):
    PYTHON = "python"
    JAVA = "java"


class AstReprType(str, Enum):
    SEXP = "sexp"
