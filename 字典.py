#唯一的映射类型
dict1 = {'xia':'jing', 'james':'xia'}
print(dict1)

#使用dict函数创建字典
dict2 = dict((('爱迪生', '天才就是天才'), ('苍井空', '姚美蝶')))   #参数是一个元组,元组的元素是元组
print(dict2)

dict3 = dict(虾米饭='保持积极乐观的人生态度', 胖红='哼哼哼')  #关键字参数的键不能带引号 
print(dict3)
print(dict3['虾米饭'])

dict4 = {-1:'负1', '正1':1}   #键值对的类型可以任意
print(dict4)
print(dict4[-1])

#如果试图访问字典中没有的key,会报错,但是如果试图修改字典中没有的key,则会生成一个新的映射
#dict4[1]
dict4[1] = 'one'
print(dict4[1])
