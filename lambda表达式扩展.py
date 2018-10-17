# lambda表达式作为参数
test = lambda x, b: x + b

num = test(1, 1)
print(num)

def test(a, b, func):
    res = func(a, b)
    return res

num = test(1, 1, lambda a, b: a + b)
print(num)
num = test(2, 1, lambda a, b: a - b)
print(num)
num = test(3, 4, lambda a, b: a * b)
print(num)

# 动态执行

func_new = eval(input("请输入一个两个参数的匿名函数："))
num = test(3, 5, func_new)
print(num)

