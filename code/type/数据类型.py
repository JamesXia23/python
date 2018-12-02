a = "123"
b = int(a)
c = float(a)
d = str(c)
print(a, b, c, d, sep="\t")

print(type(a))  #可以打印出变量的类型
print(isinstance(a, int))   #判断某个变量的类型
print(isinstance(a, str))
