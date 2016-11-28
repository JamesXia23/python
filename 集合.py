#用花括号除了可以定义字典,还可以创建一个集合(集合是无序,不重复的,不能用下标索引)

#创建集合(得到的集合是无序的)
set1 = {1, 2, 3, 4 ,3 ,4, 1}
print(set1)

set2 = set([1, 3, 3, 4, 5, 5])  #传入一个序列
print(set2)

set3 = set('xiajing')
print(set3)

#添加
set3.add('4')
print(set3)

#删除
set3.remove('4')
print(set3)

#定义一个不可变集合frozenset
set4 = frozenset(range(10))
print(set4)
#set.add(0)


