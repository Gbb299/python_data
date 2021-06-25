#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# p75 2.7 从多个文件中连接数据
import sys
import csv
import glob
import os

input_path = sys.argv[1]
output_file = sys.argv[2]

first_file = True
for input_file in glob.glob(os.path.join(input_path, 'sales_*')):
	print(os.path.basename(input_file))
	with open(input_file, 'r') as csv_in_file:
		with open(output_file, 'a') as csv_out_file:
			filereader = csv.reader(csv_in_file)
			filewriter = csv.writer(csv_out_file)
			if first_file:
				for row in filereader:
					filewriter.writerow(row)
				first_file = False
			else:
				# next 返回文件下一行
				header = next(filereader, None)
				for row in filereader:
					filewriter.writerow(row)