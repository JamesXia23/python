a = [123, "xia", '345']
for each in a:
    print(each)
print()

a.append(23.45) #在列表后面最加元素
for each in a:
    print(each)
print()

a.extend([789, 'jing']) #使用另一个列表来扩充原列表
for each in a:
    print(each)
print()

a.insert(0, 'shi')
for each in a:
    print(each)
print()
