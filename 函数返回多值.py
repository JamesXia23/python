def divid(a, b):
    q = a // b
    r = a % b
    return q, r # 返回一个元祖

q, r = divid(5, 2)
print(q, r)