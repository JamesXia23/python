aList = [1, 3, 5, 'shi', 'xia', 'jing', 3.14159]
print("aList:")
for each in aList:
    print(each)
print()

bList = aList[1:3]  #从第一个元素开始，到第2个元素，包头不包尾
print("bList:")
for each in bList:
    print(each)
print()

cList = aList[:5]   #从第零个元素开始，直到第四个元素
print("cList:")
for each in cList:
    print(each)
print()

dList = aList[3:]   #从第3个元素开始到结尾
print("dList:")
for each in dList:
    print(each)
print()

eList = aList[:]    #拷贝整个列表
print("eList:")
for each in eList:
    print(each)
print()
