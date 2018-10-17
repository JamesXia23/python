# 求无数个数的和
def sum(a, b, *args):
    print(a)
    print(b)
    print(args) # 元组

    sum_num = a + b
    for i in args:
        sum_num += i

    return sum_num

res = sum(1, 2, 3, 4, 5, 6)
print(res)
res = sum(1, 2)
print(res)

def test(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)  # 元组
    print(kwargs) # 字段

test(1, 2, 3, 4, 5, x=1, y=2)
