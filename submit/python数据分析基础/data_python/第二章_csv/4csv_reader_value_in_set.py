#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# 2.2.2 行中的值属于某个集合 p60
import csv
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
important_dates = ['1/20/14', '1/30/14']
with open(input_file, 'r') as csv_in_file:
	with open(output_file, 'w') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		# next 读出输入文件的第一
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			a_data = row_list[4]
			if a_data in important_dates:
				filewriter.writerow(row_list)
