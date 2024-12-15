import os
from pathlib import Path
import re


path = Path(os.getcwd())
input_path = path.joinpath("day3/input.txt")
with open(input_path, "r") as file:
    data = [line for line in file]

#: Part 1
res_part_1 = 0
for d in data:
    mul_finded = re.findall("mul\(*\d*,\d*\)", d)
    mul_finded_rep = [x.replace("mul(", "").replace(")", "") for x in mul_finded]
    d_res = sum(
        [float(x.split(",")[0]) * float(x.split(",")[1]) for x in mul_finded_rep]
    )
    res_part_1 += d_res


#: Part 2
#: Search mul
def multiply(mul: str):
    return float(mul.replace("mul(", "").replace(")", "").split(",")[0]) * float(
        mul.replace("mul(", "").replace(")", "").split(",")[1]
    )


mul_dict = {}
for i, d in enumerate(data):
    start_str = 0
    end_str = 0
    mul_dict[i] = {"mul": []}
    mul_search = re.search("mul\(*\d*,\d*\)", d)
    while mul_search is not None:
        mul_search = re.search("mul\(*\d*,\d*\)", d)
        if mul_search is not None:
            start_str += mul_search.start() + end_str - start_str
            end_str += mul_search.end()
            mul_dict[i]["mul"].append(
                (
                    (start_str, end_str),
                    mul_search.string[mul_search.start() : mul_search.end()],
                )
            )
            d = d[mul_search.end() :]
#: Search do
do_dict = {}
for i, d in enumerate(data):
    start_str = 0
    end_str = 0
    do_dict[i] = {"do": []}
    do_search = re.search("do\(\)", d)
    while do_search is not None:
        do_search = re.search("do\(\)", d)
        if do_search is not None:
            start_str += do_search.start() + end_str - start_str
            end_str += do_search.end()
            do_dict[i]["do"].append(
                (
                    (start_str, end_str),
                    do_search.string[do_search.start() : do_search.end()],
                )
            )
            d = d[do_search.end() :]

#: Search dont
dont_dict = {}
for i, d in enumerate(data):
    start_str = 0
    end_str = 0
    dont_dict[i] = {"dont": []}
    dont_search = re.findall("don't\(\)", data[0])
    while dont_search is not None:
        dont_search = re.search("don't\(\)", d)
        if dont_search is not None:
            start_str += dont_search.start() + end_str - start_str
            end_str += dont_search.end()
            dont_dict[i]["dont"].append(
                (
                    (start_str, end_str),
                    dont_search.string[dont_search.start() : dont_search.end()],
                )
            )
            d = d[dont_search.end() :]

res_part_2 = 0
flag_compute = True
for key in mul_dict.keys():
    list_operation = []
    list_operation.extend(mul_dict[key]["mul"])
    list_operation.extend(do_dict[key]["do"])
    list_operation.extend(dont_dict[key]["dont"])
    sorted_data = sorted(list_operation, key=lambda x: x[0][0])
    for operation in sorted_data:
        if "don" in operation[1]:
            flag_compute = False
        elif "do()" in operation[1]:
            flag_compute = True
        else:
            pass
        if flag_compute:
            if "mul" in operation[1]:
                res_part_2 += multiply(operation[1])

print("stop")
