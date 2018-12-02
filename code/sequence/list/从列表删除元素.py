aList = [1, 3, 5, "shi", "xia", "jing", 3.14159]

print("操作前：")
for each in aList:
    print(each, end = " ")
print()

aList.remove(1)
aList.remove("xia")
print("remove后：")
for each in aList:
    print(each, end = " ")
print()

del aList[1]
del aList[len(aList) - 1]
print("del后：")
for each in aList:
    print(each, end = " ")
print()

num = aList.pop(1)
print("弹出来的数据是：", num)
print("pop后：")
for each in aList:
    print(each, end = " ")
print()
