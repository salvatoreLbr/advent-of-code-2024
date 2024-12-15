import numpy as np
import os
import pandas as pd
from pathlib import Path


path = Path(os.getcwd())
input_path = path.joinpath("day1/input.csv")
input_df = pd.read_csv(input_path, sep="|")

#: First part
f1 = np.array(sorted(input_df["f1"].to_list()))
f2 = np.array(sorted(input_df["f2"].to_list()))
res_part_1 = sum(abs(f1-f2))

#: Second part
value_counts_df = input_df["f2"].value_counts().reset_index()
merge_df = pd.merge(input_df, value_counts_df, how="left", left_on=["f1"], right_on=["f2"])
merge_df["count"] = merge_df["count"].fillna(0)
res_part_2 = (merge_df["f1"]*merge_df["count"]).sum()
