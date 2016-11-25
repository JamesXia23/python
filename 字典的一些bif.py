#都是对象的成员方法
#创建一个具有相同值的字典
dict1 = {}
dict1 = dict1.fromkeys((1, 2, 3))   #如果不加第二个参数,默认值为None,返回一个新的字典
print(dict1)

dict1 = dict1.fromkeys((1, 2, 3), 'number')#字典的相同值为'number'
print(dict1)

#获取字典的key序列
print(dict1.keys()) #dict_keys([1, 2, 3])生成了一个key序列

#获取值序列
print(dict1.values())

for eachKey in dict1.keys():
    print(dict1[eachKey])

#获取字典项序列
for eachItem in dict1.items():  #会以元组的形式返回
    print(eachItem)

#用get方法来索引字典中的值时,如果找不到会返回None,不会报错
print(dict1.get(5))

#也可以指定默认值,就是找不到会返回什么
print(dict1.get(1, "小白"))#找到了就不会返回默认值
print(dict1.get(10, '小白'))#找不到就返回默认值

#获取某个键,如果没有,则创建一个,如果有值返回值
print('3:', dict1.setdefault(3))
print('5:', dict1.setdefault(5))#没有则创建一个,值默认为None
#也可以设置默认值
print('6:', dict1.setdefault(6, 'six'))

#拷贝整个字典
dict2 = dict1.copy()
print(dict2)

#删除(弹出某个元素)
print(dict1.pop(3))
print(dict1)

#随机删除某个项目
print(dict1.popitem())

#使用别的字典来更新本字典
dict1.update(dict2)
print(dict1)

#清空整个字典
dict1.clear()
print(dict1)
