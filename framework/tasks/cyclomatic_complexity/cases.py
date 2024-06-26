from framework.enums import AstReprType, ConditionType, ExecutorType, LanguageType
from framework.models import Case


def get_cases() -> list[Case]:
    cases = [
        # Case(executor=ExecutorType.GIGACHAT_LITE, condition=ConditionType.ONLY_CODE, language=LanguageType.PYTHON),
        # Case(executor=ExecutorType.GIGACHAT_LITE, condition=ConditionType.ONLY_CODE, language=LanguageType.JAVA),
        # Case(executor=ExecutorType.GIGACHAT_LITE, condition=ConditionType.ONLY_SEXP_AST, language=LanguageType.PYTHON),
        # Case(executor=ExecutorType.GIGACHAT_LITE, condition=ConditionType.ONLY_SEXP_AST, language=LanguageType.JAVA),
        # Case(executor=ExecutorType.GIGACHAT_LITE, condition=ConditionType.CODE_W_SEXP_AST, language=LanguageType.PYTHON),
        # Case(executor=ExecutorType.GIGACHAT_LITE, condition=ConditionType.CODE_W_SEXP_AST, language=LanguageType.JAVA),
        # Case(
        #     executor=ExecutorType.YANDEX_GPT_LITE,
        #     condition=ConditionType.ONLY_CODE,
        #     language=LanguageType.PYTHON,
        #     max_items=500,
        #     ast_repr_type=None,
        #     execute_delay=1,
        # ),
        # Case(
        #     executor=ExecutorType.YANDEX_GPT_LITE,
        #     condition=ConditionType.ONLY_CODE,
        #     language=LanguageType.JAVA,
        #     max_items=500,
        #     ast_repr_type=None,
        #     execute_delay=1,
        # ),
        # Case(
        #     executor=ExecutorType.YANDEX_GPT_LITE,
        #     condition=ConditionType.ONLY_SEXP_AST,
        #     language=LanguageType.PYTHON,
        #     max_items=500,
        #     ast_repr_type=AstReprType.SEXP,
        #     execute_delay=1,
        # ),
        # Case(
        #     executor=ExecutorType.YANDEX_GPT_LITE,
        #     condition=ConditionType.ONLY_SEXP_AST,
        #     language=LanguageType.JAVA,
        #     max_items=500,
        #     ast_repr_type=AstReprType.SEXP,
        #     execute_delay=1,
        # ),
        # Case(
        #     executor=ExecutorType.YANDEX_GPT_LITE,
        #     condition=ConditionType.CODE_W_SEXP_AST,
        #     language=LanguageType.PYTHON,
        #     max_items=500,
        #     ast_repr_type=AstReprType.SEXP,
        #     execute_delay=1,
        # ),
        # Case(
        #     executor=ExecutorType.YANDEX_GPT_LITE,
        #     condition=ConditionType.CODE_W_SEXP_AST,
        #     language=LanguageType.JAVA,
        #     max_items=500,
        #     ast_repr_type=AstReprType.SEXP,
        #     execute_delay=1,
        # ),
        # Case(
        #     executor=ExecutorType.PHI_MINI,
        #     condition=ConditionType.ONLY_CODE,
        #     language=LanguageType.PYTHON,
        #     max_items=500,
        #     ast_repr_type=None,
        #     execute_delay=0,
        # ),
        Case(
            executor=ExecutorType.PHI_MINI,
            condition=ConditionType.ONLY_CODE,
            language=LanguageType.JAVA,
            max_items=500,
            ast_repr_type=None,
            execute_delay=0,
        ),
        # Case(
        #     executor=ExecutorType.PHI_MINI,
        #     condition=ConditionType.ONLY_SEXP_AST,
        #     language=LanguageType.PYTHON,
        #     max_items=500,
        #     ast_repr_type=AstReprType.SEXP,
        #     execute_delay=0,
        # ),
        Case(
            executor=ExecutorType.PHI_MINI,
            condition=ConditionType.ONLY_SEXP_AST,
            language=LanguageType.JAVA,
            max_items=500,
            ast_repr_type=AstReprType.SEXP,
            execute_delay=0,
        ),
        # Case(
        #     executor=ExecutorType.PHI_MINI,
        #     condition=ConditionType.CODE_W_SEXP_AST,
        #     language=LanguageType.PYTHON,
        #     max_items=500,
        #     ast_repr_type=AstReprType.SEXP,
        #     execute_delay=0,
        # ),
        Case(
            executor=ExecutorType.PHI_MINI,
            condition=ConditionType.CODE_W_SEXP_AST,
            language=LanguageType.JAVA,
            max_items=500,
            ast_repr_type=AstReprType.SEXP,
            execute_delay=0,
        ),
        # Case(executor=ExecutorType.LLAMA_7b, condition=ConditionType.ONLY_CODE, language=LanguageType.PYTHON),
        # Case(executor=ExecutorType.LLAMA_7b, condition=ConditionType.ONLY_CODE, language=LanguageType.JAVA),
        # Case(executor=ExecutorType.LLAMA_7b, condition=ConditionType.ONLY_SEXP_AST, language=LanguageType.PYTHON),
        # Case(executor=ExecutorType.LLAMA_7b, condition=ConditionType.ONLY_SEXP_AST, language=LanguageType.JAVA),
        # Case(executor=ExecutorType.LLAMA_7b, condition=ConditionType.CODE_W_SEXP_AST, language=LanguageType.PYTHON),
        # Case(executor=ExecutorType.LLAMA_7b, condition=ConditionType.CODE_W_SEXP_AST, language=LanguageType.JAVA),
        # Case(executor=ExecutorType.CODE_LLAMA_7b, condition=ConditionType.ONLY_CODE, language=LanguageType.PYTHON),
        # Case(executor=ExecutorType.CODE_LLAMA_7b, condition=ConditionType.ONLY_CODE, language=LanguageType.JAVA),
        # Case(executor=ExecutorType.CODE_LLAMA_7b, condition=ConditionType.ONLY_SEXP_AST, language=LanguageType.PYTHON),
        # Case(executor=ExecutorType.CODE_LLAMA_7b, condition=ConditionType.ONLY_SEXP_AST, language=LanguageType.JAVA),
        # Case(executor=ExecutorType.CODE_LLAMA_7b, condition=ConditionType.CODE_W_SEXP_AST, language=LanguageType.PYTHON),
        # Case(executor=ExecutorType.CODE_LLAMA_7b, condition=ConditionType.CODE_W_SEXP_AST, language=LanguageType.JAVA),
    ]

    return cases
