#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# p62 6.2.3 的pandas重写代码

import pandas as pd
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
# startswith 用来搜索 .loc 找到相应的行或列
data_frame_value_matches_pattern = data_frame.loc[data_frame['Invoice Number'].str.startswith("001"), :]
data_frame_value_matches_pattern.to_csv(output_file, index=False)