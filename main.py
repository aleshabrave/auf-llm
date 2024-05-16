from framework.tasks.cyclomatic_complexity import case_results, reports

# case_results.execute_case_results()
reports.make_total()
reports.make_relate("yandex_gpt_lite_code_w_sexp_ast_python", "yandex_gpt_lite_only_code_python")
reports.make_relate("yandex_gpt_lite_code_w_sexp_ast_java", "yandex_gpt_lite_only_code_java")
reports.make_relate("phi_mini_code_w_sexp_ast_python", "phi_mini_only_code_python")
