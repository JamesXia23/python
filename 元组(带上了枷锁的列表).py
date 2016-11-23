#元组和列表很相似,最大的差别是元组定义了之后,不能再做修改
tuple1 = (1, 2, 3, 4, 6)
print(tuple1)
tuple2 = tuple1[2:]
print(tuple2)

tuple3 = () #空元组
#对于元组来说,小括号不是关键,逗号才是关键
tuple4 = 1, 2, 4
print(tuple4)
tuple5 = (1)
print(type(tuple5)) #只有一个小括号默认是int类型的
tuple5 = (1, )      #加一个逗号就变成元组了
print(type(tuple5))
tuple5 = 1, 
print(type(tuple5))

tuple6 = 8 * 1,     #乘法优先级比逗号高,所以是(8,)
print(tuple6)
tuple6 = 8 * (1,)   #加上括号之后就是(1, 1, 1, 1, 1, 1, 1, 1)
print(tuple6)

tuple6 = (1, 3, 5, 65, 6)   #"删除5"
tuple6 = tuple6[:2] + tuple6[3:]
print(tuple6)   #增加亦然

del tuple6      #删除整个元组(不常用,因为有回收机制)
