# 交换两个数字
a = 4
b = 5

# 第一种
# a = a + b
# b = a - b
# a = a - b

# py独有的
a, b = b, a

print("a = %d\nb = %d"%(a, b))

# 函数参数
def test(num):
    num += num  # 不等价于 num = num + num
    print(num)

num = 10
test(num)
print(num)  # 不可变参数作为对象，因为他是不可变参数，所以可以理解为值不能改变
num = [10]
test(num)   # 可变参数作为对象，相当于引用
print(num)