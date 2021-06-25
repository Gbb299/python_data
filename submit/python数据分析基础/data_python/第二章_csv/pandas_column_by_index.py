#1/uer/bin/env python3
# -*-coding:utf-8 -*-

# p64 2.3.1 列索引值 用pandas 实现

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

data_frame = pd.read_csv(input_file)
data_frame_value_in_set = data_frame.iloc[:, [0, 3]]
data_frame_value_in_set.to_csv(output_file, index=False)