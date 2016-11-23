print(dir(list))    #打印出list的bif

list1 = [1, 2, 3, 1]

print(list1.count(1))   #返回列表中某个元素出现的次数
print(list1.index(1))   #返回参数在列表中第一次出现的位置
print(list1.index(1, 3))    #第二个参数可以指定从哪个位置开始查找,同理,第三个参数可以指定查到哪里为止
list1.reverse()         #翻转列表,没有返回值
print(list1)

list2 = [1, 4, 6, 2, 3]
list2.sort()    #对列表进行默认排序
print(list2)    
list2.sort(reverse = True)
print(list2)    #逆序排序
