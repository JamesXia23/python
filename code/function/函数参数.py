#关键字参数
def fun1(exp, name):
    print(exp + " -> " + name)

fun1(name = "石夏靖", exp = "专家")

#默认参数
def fun2(name, age = 0):
    print("我叫:" + name + "今年" + str(age) + "岁")

fun2("石夏靖")
fun2("james", 21)

#收集参数(可变参数)
def fun3(*value):   #相当于定义了一个元组作为形参,所有实参都会存在这个元组中
    print(len(value))
    for each in value:
        print(each)

fun3(1, 2, 3, 'eajow', 3.15)
