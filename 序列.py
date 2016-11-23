#字符串,列表,元组都叫做序列

#将一个序列转化为list
print(list('james xia')) #['j', 'a', 'm', 'e', 's', ' ', 'x', 'i', 'a']

#将一个序列转化为tuple
print(tuple([1, 2, 3, 4, 6]))

#生成字符串
print(str(1546734))
str1 = str([1, 2, 12, 4, 5, 5])
print(type(str1))   #<class 'str'>
print(str1)         #尽管还是原样输出了,但是类型变为字符串了

#返回序列中最大值,最小值(需要序列中所有元素类型相同)
list1 = [4678, 1234, 124.67]
print(max(list1))
print(min(list1))

#求和序列(只能是数值序列)
tuple1 = (1246.456, 15714, 124)
print(sum(tuple1))

#排序序列,sorted
print(sorted(list1))

#翻转序列,reversed(生成一个序列)
print(reversed(tuple1)) #<reversed object at 0x03159530>返回一个迭代器对象,需要转换
print(list(reversed(tuple1)))   #[124, 15714, 1246.456]

#枚举序列,enumerate(生成一个序列)
list1 = [1, 12, 5, 144, 78, 145]
print(tuple(enumerate(list1))) #((0, 1), (1, 12), (2, 5), (3, 144), (4, 78), (5, 145))

#打包两个序列,zip(生成一个序列)
a = [1, 2, 3, 4, 5, 6, 7]
b = [4, 5, 7, 2, 7]
print(list(zip(a, b)))  #a中多的会省去
