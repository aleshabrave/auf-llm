import json
from collections import defaultdict
from pathlib import Path

from count_variables_task import parsers, results
from count_variables_task.models import OperationResult
from prettytable import PrettyTable


def save_special_results(path: str, operation_results: list[OperationResult]) -> None:
    results_path = Path(__file__).absolute().parents[0].joinpath(path)

    with open(results_path, "a") as results_file:
        json_results = [json.dumps(result.dict()) for result in operation_results]
        results_file.write(f'[{",".join(json_results)}]')


def save_all_results():
    algorithm_results = results.get_algorithm_results()
    save_special_results("data/algorithm_results.json", algorithm_results)

    gigachat_wo_ast_results = results.get_gigachat_wo_ast_results()
    save_special_results("data/gigachat_wo_ast_results.json", gigachat_wo_ast_results)

    gigachat_w_json_ast_results = results.get_gigachat_w_json_ast_results()
    save_special_results(
        "data/gigachat_w_json_ast_results.json", gigachat_w_json_ast_results
    )

    get_gigachat_w_sexp_ast_results = results.get_gigachat_w_sexp_ast_results()
    save_special_results(
        "data/gigachat_w_sexp_ast_results.json", get_gigachat_w_sexp_ast_results
    )


def _calculate_accurancy(source: list[OperationResult], target: list[OperationResult]):
    mistakes = 0
    total = 0

    for source_result in source:
        try:
            int(source_result.result)
            total += 1
        except:
            continue

        for target_result in target:
            if (
                source_result.code_snippet.snippet_id
                == target_result.code_snippet.snippet_id
            ):
                break

        try:
            int(target_result.result)
        except:
            total -= 1
            continue

        if int(source_result.result) != int(target_result.result):
            mistakes += 1

    return total - mistakes, mistakes, total, (total - mistakes) / total


def calculate_accurancy():
    algorithm_results = parsers.get_results("data/algorithm_results.json")
    gigachat_wo_ast_results = parsers.get_results("data/gigachat_wo_ast_results.json")
    gigachat_w_json_ast_results = parsers.get_results(
        "data/gigachat_w_json_ast_results.json"
    )
    gigachat_w_json_ast_results_explain_var = parsers.get_results(
        "data/gigachat_w_json_ast_results_explain_var.json"
    )
    gigachat_w_sexp_ast_results = parsers.get_results(
        "data/gigachat_w_sexp_ast_results.json"
    )
    gigachat_w_sexp_ast_results_explain_var = parsers.get_results(
        "data/gigachat_w_sexp_ast_results_explain_var.json"
    )

    total_results = defaultdict(list)
    total_results["algo_vs_gigachat_wo_ast"] += [
        *_calculate_accurancy(algorithm_results, gigachat_wo_ast_results)
    ]
    total_results["algo_vs_gigachat_w_json_ast"] += [
        *_calculate_accurancy(algorithm_results, gigachat_w_json_ast_results)
    ]
    total_results["algo_vs_gigachat_w_json_ast_w_explain_var"] += [
        *_calculate_accurancy(
            algorithm_results, gigachat_w_json_ast_results_explain_var
        )
    ]
    total_results["algo_vs_gigachat_w_sexp_ast"] += [
        *_calculate_accurancy(algorithm_results, gigachat_w_sexp_ast_results)
    ]
    total_results["algo_vs_gigachat_w_sexp_ast_w_explain_var"] += [
        *_calculate_accurancy(
            algorithm_results, gigachat_w_sexp_ast_results_explain_var
        )
    ]

    return total_results

def save_total_accurancy_result(path: str = "result.txt"):
    accurancy = calculate_accurancy()
    result_path = Path(__file__).absolute().parents[0].joinpath(path)

    table = PrettyTable(field_names=["vs_name", "correct", "mistakes", "total", "accurancy"])

    for vs_name, result in accurancy.items():
        table.add_row([vs_name, *result])
    
    with open(result_path, "w") as result_file:
        result_file.write(table.get_string())

def main() -> None:
    save_total_accurancy_result()
