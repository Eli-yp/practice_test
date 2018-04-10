n = int(input())    #输入一个整数
s = []        #定义一个空列表
for i in range(n):
	s.append(input())    #将输入的字符串添加到列表
l = sorted(s)        #将列表排序
for i in l:    
	print(i)        #依次输出
