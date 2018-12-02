a = 100
b = a

print(id(a))
print(id(b)) # 两者的地址相同，b = a就是b引用了a的地址

A = [11, 22, 33]
B = A   # 同样是引用
A.append(44)
print(B)

# py只要涉及到赋值的地方，都是引用