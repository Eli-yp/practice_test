#输入一个正浮点数。小数点后面的数大于5则向上取整

n = float(input())
l = (int(n) * 2 + 1) / 2
if n < l:
	print(int(n))
else:
	print(int(n+1))
