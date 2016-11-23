list1 = ['123']
list2 = [123]
#print(list1 < list2)   #不能比较,因为第一个元素不是同一类型的

list3 = ['123', 456]
print(list1 < list3)    #列表比较从第一个开始比较,只要第一个小于即可

list4 = list1 + list3
print(list4)
print(list4 * 3)
list5 = ['xia', 'mi']
list4.append(list5)
print(list4)
print('xia' in list4)
print('xia' in list4[3])
print(list4[3][1])

