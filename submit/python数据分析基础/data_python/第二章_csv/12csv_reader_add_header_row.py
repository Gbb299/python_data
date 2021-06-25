#!/usr/bin/dev python3
# -*- coding:utf-8 -*-

# p69 2.5 添加行标题
import csv
import sys

input_file = sys.argv[1]
output_file = sys.argv[2]

with open(input_file, 'r') as csv_in_file:
	with open(output_file, 'w') as csv_out_file:
		filereader = csv.reader(csv_in_file)
		filewriter = csv.writer(csv_out_file)
		header_list = ['Supplier Name', 'Invoice Number', 'Part Number', 'Cost', 'Purchase Date']
		filewriter.writerow(header_list)
		# filewriter 是一个空文件，才写入了标题，还要将input_file 里的其它数据写进去
		for row in filereader:
			print(row)
			filewriter.writerow(row)