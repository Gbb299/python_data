#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import csv
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
with open(input_file, 'r') as csv_in_file:
	with open(output_file, 'w') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		# next 读出输入文件的第一
		header = next(filereader)
		filewriter.writerow(header)
		for row_list in filereader:
			supplier = str(row_list[0]).strip()
			cost = str(row_list[3]).strip('$').replace(',', '')
			if supplier == 'Supplier Z' and float(cost) > 600.0:
				filewriter.writerow(row_list)
