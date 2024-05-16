from pathlib import Path

from prettytable import PrettyTable

from framework.models import AssertResult
from framework.tasks.cyclomatic_complexity import case_results


def make_relate(
    source_name: str,
    relate_name: str,
    data_dir: str = "data",
    report_dir: str = "report",
) -> None:

    assert_results: list[AssertResult] = []
    source_code_snippet_ids: set[int] = set()

    for case, execute_results in case_results.get_case_results(data_dir):
        if str(case) != source_name:
            continue

        clean_total = 0
        mistakes = 0
        execute_result_sum = 0
        eps_1_mistakes = 0
        eps_2_mistakes = 0
        eps_3_mistakes = 0

        for execute_result in execute_results:
            baseline_result = case_results.get_baseline_result(
                execute_result.code_snippet
            )
            source_code_snippet_ids.add(execute_result.code_snippet.id)

            execute_result_buff = []

            for i in execute_result.text.strip():
                try:
                    int(i)
                    execute_result_buff.append(i)
                except:
                    pass

            if not execute_result_buff:
                continue

            execute_result_num = int("".join(execute_result_buff))

            if baseline_result != execute_result_num:
                mistakes += 1

            execute_result_sum += abs(execute_result_num - baseline_result)

            if 1 < abs(execute_result_num - baseline_result):
                eps_1_mistakes += 1

            if 2 < abs(execute_result_num - baseline_result):
                eps_2_mistakes += 1

            if 3 < abs(execute_result_num - baseline_result):
                eps_3_mistakes += 1

            clean_total += 1

        accuracy = (
            (clean_total - mistakes) / clean_total if clean_total > 0 else 10_000_000
        )
        mae = execute_result_sum / clean_total if clean_total > 0 else 10_000_000

        eps_1_accuracy = (
            (clean_total - eps_1_mistakes) / clean_total
            if clean_total > 0
            else 10_000_000
        )
        eps_2_accuracy = (
            (clean_total - eps_2_mistakes) / clean_total
            if clean_total > 0
            else 10_000_000
        )
        eps_3_accuracy = (
            (clean_total - eps_3_mistakes) / clean_total
            if clean_total > 0
            else 10_000_000
        )

        assert_results.append(
            AssertResult(
                name=str(case),
                clean_total=clean_total,
                total=case.max_items,
                mistakes=mistakes,
                accuracy=round(accuracy, 4),
                mae=round(mae, 4),
                eps_1_accuracy=round(eps_1_accuracy, 4),
                eps_2_accuracy=round(eps_2_accuracy, 4),
                eps_3_accuracy=round(eps_3_accuracy, 4),
            )
        )
        break

    for case, execute_results in case_results.get_case_results(data_dir):
        if str(case) != relate_name:
            continue

        clean_total = 0
        mistakes = 0
        execute_result_sum = 0
        eps_1_mistakes = 0
        eps_2_mistakes = 0
        eps_3_mistakes = 0

        for execute_result in execute_results:
            if execute_result.code_snippet.id not in source_code_snippet_ids:
                continue

            baseline_result = case_results.get_baseline_result(
                execute_result.code_snippet
            )
            source_code_snippet_ids.add(execute_result.code_snippet.id)

            execute_result_buff = []

            for i in execute_result.text.strip():
                try:
                    int(i)
                    execute_result_buff.append(i)
                except:
                    pass

            if not execute_result_buff:
                continue

            execute_result_num = int("".join(execute_result_buff))

            if baseline_result != execute_result_num:
                mistakes += 1

            execute_result_sum += abs(execute_result_num - baseline_result)

            if 1 < abs(execute_result_num - baseline_result):
                eps_1_mistakes += 1

            if 2 < abs(execute_result_num - baseline_result):
                eps_2_mistakes += 1

            if 3 < abs(execute_result_num - baseline_result):
                eps_3_mistakes += 1

            clean_total += 1

        accuracy = (
            (clean_total - mistakes) / clean_total if clean_total > 0 else 10_000_000
        )
        mae = execute_result_sum / clean_total if clean_total > 0 else 10_000_000

        eps_1_accuracy = (
            (clean_total - eps_1_mistakes) / clean_total
            if clean_total > 0
            else 10_000_000
        )
        eps_2_accuracy = (
            (clean_total - eps_2_mistakes) / clean_total
            if clean_total > 0
            else 10_000_000
        )
        eps_3_accuracy = (
            (clean_total - eps_3_mistakes) / clean_total
            if clean_total > 0
            else 10_000_000
        )

        assert_results.append(
            AssertResult(
                name=str(case),
                clean_total=clean_total,
                total=case.max_items,
                mistakes=mistakes,
                accuracy=round(accuracy, 4),
                mae=round(mae, 4),
                eps_1_accuracy=round(eps_1_accuracy, 4),
                eps_2_accuracy=round(eps_2_accuracy, 4),
                eps_3_accuracy=round(eps_3_accuracy, 4),
            )
        )

        break

    report_name = f"{source_name}-{relate_name}-relate-report.txt"
    _save(assert_results, report_dir, report_name)

    print("Report was successful made")


def make_total(
    data_dir: str = "data",
    report_dir: str = "report",
    report_name: str = "total-report.txt",
) -> None:

    assert_results: list[AssertResult] = []

    for case, execute_results in case_results.get_case_results(data_dir):
        clean_total = 0
        mistakes = 0
        execute_result_sum = 0
        eps_1_mistakes = 0
        eps_2_mistakes = 0
        eps_3_mistakes = 0

        for execute_result in execute_results:
            baseline_result = case_results.get_baseline_result(
                execute_result.code_snippet
            )

            execute_result_buff = []

            for i in execute_result.text.strip():
                try:
                    int(i)
                    execute_result_buff.append(i)
                except:
                    pass

            if not execute_result_buff:
                continue

            execute_result_num = int("".join(execute_result_buff))
            # try:
            #     execute_result_num = int(execute_result.text.strip())
            # except:
            #     continue

            if baseline_result != execute_result_num:
                mistakes += 1

            execute_result_sum += abs(execute_result_num - baseline_result)

            if 1 < abs(execute_result_num - baseline_result):
                eps_1_mistakes += 1

            if 2 < abs(execute_result_num - baseline_result):
                eps_2_mistakes += 1

            if 3 < abs(execute_result_num - baseline_result):
                eps_3_mistakes += 1

            clean_total += 1

        accuracy = (
            (clean_total - mistakes) / clean_total if clean_total > 0 else 10_000_000
        )
        mae = execute_result_sum / clean_total if clean_total > 0 else 10_000_000

        eps_1_accuracy = (
            (clean_total - eps_1_mistakes) / clean_total
            if clean_total > 0
            else 10_000_000
        )
        eps_2_accuracy = (
            (clean_total - eps_2_mistakes) / clean_total
            if clean_total > 0
            else 10_000_000
        )
        eps_3_accuracy = (
            (clean_total - eps_3_mistakes) / clean_total
            if clean_total > 0
            else 10_000_000
        )

        assert_results.append(
            AssertResult(
                name=str(case),
                clean_total=clean_total,
                total=case.max_items,
                mistakes=mistakes,
                accuracy=round(accuracy, 4),
                mae=round(mae, 4),
                eps_1_accuracy=round(eps_1_accuracy, 4),
                eps_2_accuracy=round(eps_2_accuracy, 4),
                eps_3_accuracy=round(eps_3_accuracy, 4),
            )
        )

    _save(assert_results, report_dir, report_name)

    print("Report was successful made")


def _save(
    assert_results: list[AssertResult], report_dir: str, report_name: str
) -> None:
    result_path = (
        Path(__file__).absolute().parents[0].joinpath(f"{report_dir}/{report_name}")
    )

    assert_result_field_names = list(AssertResult.model_fields.keys())

    table = PrettyTable(field_names=assert_result_field_names)

    for assert_result in assert_results:
        values = []
        for field_name in assert_result_field_names:
            values.append(assert_result.__getattribute__(field_name))

        table.add_row(values)

    with open(result_path, "w") as result_file:
        result_file.write(table.get_string())
