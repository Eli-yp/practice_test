#将字符串按每8个字分割，不足8的的在后面补0

def split_8(n):       #定义分割字符串的函数
	l = len(n)
	if l < 8:			#如果字符长度小于8
		r = 8 - l
		for i in range(r):
			n = n + '0'		#在字符串后面加0
		print(n)

	if l == 8:
		print(n)			#如果字符串产度为8,则原样输出

	if l > 8:		#长度大于8
		a = l // 8			#取出倍数
		for i in range(a):
			print(n[i*8 : (i+1)*8])  #输出前面a倍的
		b = l % 8	#取出摸
		if b > 0:
			print(n[-b:]+'0'*(8-b))		#在后面补0

a = input()
b = input()
split_8(a)
split_8(b)
