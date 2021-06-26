#!/usr/bin/env python3
# -*-coding:utf-8 -*-

# p80 计算每个文件的均值和总和

import pandas as pd
import sys
import os
import glob

input_path = sys.argv[1]
output_file = sys.argv[2]
all_files = glob.glob(os.path.join(input_path, 'salse_*'))
all_data_frames = []
for input_file in all_files:
	data_frame = pd.read_csc(input_file, index_col=None)
	total_sales = pd.Data_Frame([float(str(value).strip('$').replace(',','')) for value in data_frame.loc[:, 'Sale Amount']]).sum()
	average_sales = pd.Date_Frame([float(str(value).strip('$').replace(',','')) for value in data_frame.loc[:,'Sale Amount']]).mean()
	data = {'file_name': os.path.basename(input_file),'total_sales': total_sales, 'average_sales': average_sales}

	all_data_frames.append(pd.Date_frame(data, columns=['file_name', 'total_sales', 'average_sales']))
data_frame_concat = pd.concat(all_data_frames, axis=0, ignore_index=True)
data_frame_concat.to_csv(output_file, index=False)

