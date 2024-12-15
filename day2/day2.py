import numpy as np
import os
from pathlib import Path


path = Path(os.getcwd())
input_path = path.joinpath("day2/input.txt")
with open(input_path, "r") as file:
    data = [list(map(float, line.split())) for line in file]

#: Part 1
# The levels are either all increasing or all decreasing
# Any two adjacent levels differ by at least one and at most three
check_1_array = [
    sum(
        [
            ((data_report[i + 1] - data_report[i]) > 0)
            and ((data_report[i + 1] - data_report[i]) <= 3)
            for i in range(len(data_report) - 1)
        ]
    )
    == len(data_report) - 1
    for data_report in data
]
check_2_array = [
    sum(
        [
            ((data_report[i + 1] - data_report[i]) < 0)
            and ((data_report[i + 1] - data_report[i]) >= -3)
            for i in range(len(data_report) - 1)
        ]
    )
    == len(data_report) - 1
    for data_report in data
]
res_part_1 = sum(check_1_array) + sum(check_2_array)

#: Part 2
# if removing a single level from an unsafe report would make it safe, the report instead counts as safe
#: Get the actual unsafe report
[(i, x) for i, x in enumerate(check_1_array) if x == True]

unsafe_report = np.array(check_1_array) + np.array(check_2_array)
unsafe_report_id = [i for i, x in enumerate(unsafe_report) if x == False]
new_safe_report_id = []
for i_i in unsafe_report_id:
    data_report = data[i_i]
    for x in range(len(data_report)):
        data_report_x = data_report.copy()
        data_report_x.pop(x)
        check_1_array_x = (
            sum(
                [
                    ((data_report_x[i + 1] - data_report_x[i]) > 0)
                    and ((data_report_x[i + 1] - data_report_x[i]) <= 3)
                    for i in range(len(data_report_x) - 1)
                ]
            )
            == len(data_report_x) - 1
        )
        check_2_array_x = (
            sum(
                [
                    ((data_report_x[i + 1] - data_report_x[i]) < 0)
                    and ((data_report_x[i + 1] - data_report_x[i]) >= -3)
                    for i in range(len(data_report_x) - 1)
                ]
            )
            == len(data_report_x) - 1
        )
        if check_1_array_x or check_2_array_x:
            new_safe_report_id.append(i_i)
            continue
new_safe_report = len(list(set(new_safe_report_id)))
res_part_2 = res_part_1 + new_safe_report
