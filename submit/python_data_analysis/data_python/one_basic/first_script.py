#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from math import exp, log, sqrt
import re
from datetime import date, time, datetime, timedelta
from operator import itemgetter
import sys
print("Output #1: i'm exciting learn python")

x = 4
y = 5 
z = x + y
print("Output #2: Four plus five equals {0:d}.".format(z))


# 两个列表相加

a = [1, 2, 3]
b = ["first", "second", "third", "fourth"]
c = a + b
print("Output #3: {0}, {1}, {2}".format(a, b, c))

# 1.4.1 数值
# 1. 整数
x = 9
print("Output #4: {0}".format(x))
print("Output #5: {0}".format(3**4))
print("Output #6: {0}".format(int(8.3)/int(2.7)))

# 2. 浮点数
print("Output #7: {0:.3f} ".format(8.3/2.7))
y = 2.5*4.8
print("Output #8: {0:.1f} ".format(y))
r = 8/float(3)
print("Output #9: {0:.2f} ".format(r))
print("Output #10: {0:.4f}".format(8.0/3))


# 引入math
print("Output #11: {0:.4f}".format(exp(3)))
print("Output #12: {0:.2f}".format(log(4)))
print("Output #13: {0:.1f}".format(sqrt(81)))

# 1.4.2 字符串

print("Output #14: {0:s}".format('i\'m enjoying learning python'))

string1 = "My deliverable is due in May"
string1_list1 = string1.split()
string1_list2 = string1.split(' ',2)
print("Output #21: {0}".format(string1_list1))
print("Output #22: FIRST PIECE: {0} SECOND PIECE: {1} THIRD PIECE: {2}"\
	.format(string1_list2[0], string1_list2[1], string1_list2[2]))


string2 = "Your,deliverable,is,due,in,May"
string2_list = string2.split(',')
print("Output #23: {0}".format(string2_list))

# 2. join

print("Output #25: {0}".format('-'.join(string2_list)))

# 3. strip

string3 = " Remove unwanted characters    from this string. \t\t  \n"
print("Output #26: string3: {0:s}".format(string3))
# 去除左侧空格
string3_lstrip = string3.lstrip()
print("Output #27: string3_lstrip: {0:s}".format(string3_lstrip))
# 去除右侧空格
string3_rstrip = string3.rstrip()
print("Output #28: string_rstrip: {0:s}".format(string3_rstrip))
string3_strip = string3.strip()
print("Output #29: string_strip: {0:s}".format(string3_strip))


# 从字符串两端删除其他字符串的方法

string4 = "$$Here's another string $ that has unwanted characters._----++"
print("Output #30: {0:s}".format(string4))
string4_strip = string4.strip('$_-+')
print("Output #31: {0:s}".format(string4_strip))

# 4. replace 替换字符串
string5 = "Let's replace the space in this sentence with other characters."
string5_replace = string5.replace(' ', '$!!')
print("Output #32: (with $!!): {0:s}".format(string5_replace))
string5_replace = string5.replace(' ', ',')
print("Output #33: (with commas); {0:s}".format(string5_replace))


# lower upper and capitalize
string6 = "Here's WHAT Happens WHEN You Use lower"
print("Output #34: {0:s}".format(string6.lower()))
string7 = "here's what happens when you use UPPER"
print("Output #35: {0:s}".format(string7.upper()))
string5 = "here's WHAT Happens WHEN You Use lower"
print("Output #36: {0:s}".format(string5.capitalize()))
string5_list = string5.split()
print("Output #37: (on each word):")
for word in string5_list:
	print("{0:s}".format(word.capitalize()))



# 2021-6-15 
# 正则表达式与模式匹配

# 计算字符串中模式出现的次数
string = "The quick brown fox jumps over the lazy dag."
string_list = string.split()
pattern = re.compile(r'The', re.I)
count = 0
for word in string_list:
	if pattern.search(word):
		count += 1
print("Output #38: {0:d}".format(count))


# 将找到的字符串打印出来
string = "The quick brown fox jumps over the lazy dag."
string_list = string.split()
pattern = re.compile(r"(?P<match_word>The)", re.I)
print("Output #39:")
for word in string_list:
	if pattern.search(word):
		print("{0:s}".format(pattern.search(word).group('match_word')))

# 使用字母 a 替换 the

string = "The quick brown fox jumps over the lazy dag."
string_to_find = r"The"
pattern = re.compile(string_to_find, re.I)
print("Output #40: {0:s}".format(pattern.sub("a", string)))



# 1.4.4 日期
today = date.today()
print("Outout #41: today: {0!s}".format(today))
print("Outout #42:  {0!s}".format(today.year))
print("Outout #43:  {0!s}".format(today.month))
print("Outout #44:  {0!s}".format(today.day))
current_datetime = datetime.today()
print("Output #45: {0!s}".format(current_datetime))

# 使用timedelta 计算一个新日期
one_day = timedelta(days=-1)
yesterday = today + one_day
print("Output: #46: yesterdat: {0!s}".format(yesterday))
eight_hours = timedelta(days=-8)
print("Output: #47: {0!s}, {0!s}".format(eight_hours.days, eight_hours.seconds))

# 计算两个日期之间的天数
date_diff = today - yesterday
print("Output #48: {0!s}".format(date_diff))
print("Output #49: {0!s}".format(str(date_diff).split()[0]))

# 创建特定格式字符串
print("Output #50: {:s}".format(today.strftime('%m/%d/%y')))



# 2021-6-16
# -------------------------------
# 1.4.5 列表

# 1. 创建列表

a_list = [1, 2, 3]
print("Output #58: {}".format(a_list))
print("Output #59: the a_list has {} elements.".format(len(a_list)))
print("Output #60: the maximum value in a_list is {}".format(max(a_list)))
print("Output #61: the minimum value in a_list is {}".format(min(a_list)))
another_list = ['printer', 5, ['start', 'circle', 9]]
print("Output #62: {}".format(another_list))
print("Output #63: another_list has also {} elements".format(len(another_list)))
print("Output #64: 5 is in another_list {} time".format(another_list.count(5)))

# 索引值
# 使用索引值访问列表中特定的元素
print("Output #65: {}".format(a_list[0]))

# 3.列表切片
print("Output #73: {}".format(a_list[:2]))
# 使用 [:] 复制一个liebiao

a_new_list = a_list[:]
print("Output #77: {}".format(a_new_list))


# 使用 + 将两个或多个列表连接起来
a_another_list = a_list + another_list
print("Output #78: {}".format(a_another_list))

# 使用 in 和 not in 来检查列表中是否有特定的yuanus
a = 2 in a_another_list
print("Out put #79: {}".format(a))
if 2 in a_list:
	print("Output #80: 2 is in {}".format(a_list))
b = 6 not in a_list
print("Output #81: {}".format(b))
if 6 not in a_list:
	print("Output #82: 6 not in {}".format(a_list))

# append() 向列表末尾追加元素
# remove() 从列表中删除特定的元素
# pop() 从末尾删除一个元素

a_list.append(4)
a_list.append(5)
a_list.append(6)
print("Output #83: {}".format(a_list))
a_list.remove(5)
print("Output #84: {}".format(a_list))

a_list.pop()
a_list.pop()
print("Output #84: {}".format(a_list))

# 使用reverse 原地反转一个列表会修改原列表
# 想反转列表的同时又不修改原列表 可以使用复制

a_list.reverse()
print("Output #86: {}".format(a_list))
a_list.reverse()
print("Output #87: {}".format(a_list))

# 列表排序
# sort() 排序会修改原列表
unordered_list = [3, 5, 1, 7, 2, 8, 4, 9, 0, 6]
print("Output #88: {}".format(unordered_list))
list_copy = unordered_list[:]
list_copy.sort()
print("Output #89: {}".format(list_copy))
print("Output #90: {}".format(unordered_list))

# 10. sorted 排序函数
# 使用sorted()对一个列表集合按照列表中某个位置的元素进行排序
my_lists = [[1,2,3,4], [4,3,2,1], [2,4,1,3]]
my_lists_sorted_by_index_3 = sorted(my_lists, key=lambda index_value: index_value[3])
print("Output #91: {}".format(my_lists_sorted_by_index_3))
# 索引位置为 3 的位置进行排序
# sorted 返回一个新的列表

# 使用 itemgetter 对列表集合按照两个索引位置排序
my_list = [[123,2,2,444], [22,6,6,444],[354,4,4,678], [236,5,5,678], \
[578,1,1,290], [461,1,1,290]]
my_list_sorted_by_index_3_0 = sorted(my_list, key=itemgetter(3,0))
print("Output #92: {}".format(my_list_sorted_by_index_3_0))



# 2021-6-17 晚上
# ------------------------------
# 1.4.6 元组

# 1. 创建元组
# 使用圆括号创建元组
my_tuple = ('x', 'y', 'z')
print("Output #93: {}".format(my_tuple))
print("Output #94: my_tuple has {} elements".format(len(my_tuple)))
print("Output #95: {}".format(my_tuple[1]))
longer_tuple = my_tuple + my_tuple
print("Output #96: {}".format(longer_tuple))

# 2. 元组解包
one, two, three = my_tuple
print("Output #97: {0}, {1}, {2}".format(one, two, three))
var1 = 'red'
var2 = 'robin'
print("Output #98: {}, {}".format(var1, var2))

# 在变量之间彼此交换值

var1, var2 = var2, var1
print("Output #99: {}, {}".format(var1, var2))

# 1.4.7 字典

# 1. 创建字典
# 2. 使用 ： 分隔键-值对
# 3. 用len 计算数量
empty_dict = {}
a_dict = {'one':1, 'two':2, 'three':3}
print("Output #102: {}".format(a_dict))
print("Output #103: a_dict has {} elements".format(len(a_dict)))
another_dict = {'x':'printer', 'y':5, 'z':['start', 'circle', 9]}
print("Output #104: {}".format(another_list))
print("Output #105: another_dict has {} elements".format(len(another_dict)))

# 2. 引用字典中的值
# 使用键来引用字典中的特定的值
print("Output #106: {}".format(a_dict['two']))
# 键值的类型是 --> 字符串
print("Output #107: {}".format(another_dict['z']))

# 使用copy（）复制字典
a_new_dict = a_dict.copy() 
print("Output #108: {}".format(a_new_dict)) 

# 键， 值， 项目
# 使用 keys(), value(), items()
# 分别引用 字典中的 键 值 键-值
print("Output #109: {}".format(a_dict.keys()))
a_dict_keys = a_dict.keys()
print("Output #110: {}".format(a_dict_keys))
print("Output #111: {}".format(a_dict.values()))
print("Output #112: {}".format(a_dict.items()))

# 使用 in not in and get 
if 'y' in another_dict:
	print("Output #113: 'y' is a key in another_dict: {}".format(another_dict.keys()))
if 'c' not in another_dict:
	print("Output #114 'c' is not a key in anther_dict: {}".format(another_dict.keys()))
# get() 返回键值对应的字典值
print("Output #116: {!s}".format(a_dict.get('three')))
print("Output #117: {!s}".format(a_dict.get('four')))
print("Output #118: {!s}".format(a_dict.get('four', 'Not in dict')))

# 6. 排序
# 使用 sorted 对字典进行排序
# 要想对字典排序的同时不修改原字典
# 复制字典
print("Output #119: {}".format(a_dict))
dict_copy = a_dict.copy()
ordered_dict1 = sorted(dict_copy.items(), key=lambda item: item[0])
print("Output #120: (order by keys): {}".format(ordered_dict1))
ordered_dict2 = sorted(dict_copy.items(), key=lambda item: item[1])
print("Output #121: (order by value): {}".format(ordered_dict2))
ordered_dict3 = sorted(dict_copy.items(), key=lambda X: X[1], reverse=True)
print("Output #122: (order by value ,descending: {}".format(ordered_dict3))
ordered_dict4 = sorted(dict_copy.items(), key=lambda X: X[1], reverse=False)
print("Output #123: (ordered by value, ascending: {}".format(ordered_dict4))



# 2021-6-18 傍晚 
#--------------------

# 1.4.8 控制流
# 1. if-else 语句
x = 5
if x > 4 :
	print("Output #124: {}".format(x))
else:
	print("Output #124: x is not greater then 4")

# if-elif-else

if x > 6:
	print("Output #125: x is greater than six")
elif x > 4 and x == 5:
	print("Output #125: {}".format(x*x))
else:
	print("Output #125: x is not greater than 4")

# 3. for循环

y = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
z = ['Annie', 'Betty', 'Claire', 'Daphne', 'Ellie', 'Franchesca', 'Grata', 'Holly', 'Isabel', 'Jenny']

print("Output #126:")
for month in y:
	print("{!s}".format(month))

print("Output #127: (index value: name in list")
for i in range(len(z)):
	print("{0!s}: {1:s}".format(i, z[i]))

print("Output #128: (access elements in y with z's index values) ")
for j in range(len(z)):
	if y[j].startswith('J'):
		print("{!s}".format(y[j]))


print("Output #129:")
for key, value in another_dict.items():
	print("{0}, {1}".format(key, value))

# 4. 简化for循环：列表， 集合， 字典生成式
# 列表生成式
# 使用列表生成式选择特定的行
my_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rows_to_keep = [row for row in my_data if row[2] > 5]
print("Ouput #130: (list comprehension): {}".format(rows_to_keep))

# 集合生成式
# 使用集合生成式在列表中选择唯一的元组
my_data = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (7, 8, 9)]
set_of_tuples1 = {x for x in my_data}
print("Output #131: (list comprehension): {}".format(set_of_tuples1))
set_of_tuples2 = set(my_data)
print("Output #132: (set function): {}".format(set_of_tuples2))


# 使用字典生成式选择特定的键-值对
my_dictionary = {'customer1': 7, 'customer2': 8, 'customer3': 11}
my_results = {key : value for key, value in my_dictionary.items() if value > 10}
print("Output #133: (dictionary comprehension {}".format(my_results))


# 5. while 循环

print("output #134: ")
x = 0 
while x < 11:
	print("{}".format(x))
	x += 1

# 6. 函数
# 计算一系列数值的均值
def getMean(numericValues):
	return sum(numericValues)/len(numericValues) if len(numericValues) > 0 else float('nan')
my_list = [2, 3, 5]
print("output: #135 (mean): {!s}".format(getMean(my_list))) 


# 2021-6-19

def getMean(numericValues):
	return sum(numericValues)/len(numericValues)  

my_list2 = [1, 2]

try:
	print("Output #138: {}".format(getMean(my_list2)))
except ZeroDivisionError as detail:
	print("Output #138: (Error): {}".format(float('nan')))
	print("Output: #138: (Error) {}".format(detail))


# 9. try-except-else-finally
try:
	result = getMean(my_list2)
except ZeroDivisionError as detail:
	print("Output #138: (Error): {}".format(float('nan')))
	print("Output: #138: (Error) {}".format(detail))
else:
	print("Output #142: (the mean is): {}".format(result))
finally:
	print("Output #142: (finally) The finally block is executed every time")


# 读取文件
# 读取单个文件

# input_file = sys.argv[1]

# print("Output #142:")
# filereader = open(input_file, 'r')
# for row in filereader:
# 	print(row.strip())
# filereader.close()




