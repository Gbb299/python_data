#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import glob
import os

# input_file = sys.argv[1]

# print("Output #142:")
# filereader = open(input_file, 'r')
# for row in filereader:
# 	print(row.strip())
# filereader.close()


# input_file = sys.argv[1]

# print("Output #144:")
# with open(input_file, 'r') as filereader:
# 	for row in filereader:
# 		print("{}".format(row.strip()))


# print("Output #145: ")
# inputPath = sys.argv[1]
# for input_file in glob.glob(os.path.join(inputPath, '*.txt')):
# 	with open(input_file, 'r') as filereader:
# 		for row in filereader:
# 			print("{}".format(row.strip()))

# 1.7 写入文件
# 1.7.1 向 first_script.py 添加代码
# 写入文件
# 写入一个文本文件

# my_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
# max_index = len(my_letters)
# output_file = sys.argv[1]
# filewriter = open(output_file, 'w')
# for index_value in range(len(my_letters)):
# 	if index_value < (max_index - 1):
# 		filewriter.write(my_letters[index_value]+'\t')
# 	else:
# 		filewriter.write(my_letters[index_value]+'\n')
# filewriter.close()
# print("Output #146: Output written to file")

# 1.7.2 写入csv文件

my_numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
max_index = len(my_numbers)
input_file = sys.argv[1]
filewrite = open(input_file, 'a')
for index_value in range(len(my_numbers)):
	if index_value < (max_index - 1):
		filewrite.write(str(my_numbers[index_value])+',')
	else:
		filewrite.write(str(my_numbers[index_value])+'\n')
filewrite.close()
print("Output #147: Output appended to file")