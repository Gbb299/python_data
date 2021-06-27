#!/usr/bin/env python3 
# -*- coding:utf-8 -*-

# p64 2.3.1 选取特定的列

import csv
import sys
input_file = sys.argv[1]
output_file = sys.argv[2]
my_columns = [0, 3]
with open(input_file, 'r') as csv_in_file:
	with open(output_file, 'w') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		for row_list in filereader:
			# x = row_list[0]
			# y = row_list[3]
			# row_list_output = []
			# row_list_output.append(x)
			# row_list_output.append(y)
			# filewriter.writerow(row_list_output)
			# print(row_list)
			row_list_output = []
			for index_value in my_columns:
				row_list_output.append(row_list[index_value])
			filewriter.writerow(row_list_output)


