#!/usr/bin/env python3 
# -*- coding:utf-8 -*-

# 4.2 选取连续行 用 pandas 实现

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
data_frame = data_frame.drop([0, 1, 2, 15, 16, 17])
# data_frame.columns = data_frame.iloc[0]
data_frame = data_frame.reindex(data_frame.index.drop(3))
data_frame.to_csv(output_file, index=False)
