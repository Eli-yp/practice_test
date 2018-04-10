#提取不重复的整数

#-*- coding:utf-8 -*-

s = input() #输入一连串数字
l = list(s)	#将其转换成列表
l =  l[::-1]	#将其逆序
r = []
for i in l:
	if i not in r:   #将不重复的数字取出来
		r.append(i)
print(''.join(r))	#打印列表
