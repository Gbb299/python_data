#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# p69 2.5 添加行标题（用pandas 实现）

import pandas as pd
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]
header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Number']

data_frame = pd.read_csv(input_file, header=None, names=header_list)
data_frame.to_csv(output_file, index=False)