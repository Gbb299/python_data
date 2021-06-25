#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# p61 2.pandas 用pandas实现行中的值属于某个集合

import pandas as pd
import sys 
input_file = sys.argv[1]
output_file = sys.argv[2]
data_frame = pd.read_csv(input_file)
important_dates = ['1/20/14', '1/30/14']
data_frame_value_in_set = data_frame.loc[data_frame['Purchase Date'].isin(important_dates), :]
data_frame_value_in_set.to_csv(output_file, index=False)