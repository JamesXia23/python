gb = 123

def fun1():
    # print(gb)  #如果函数下面有声明一个跟全局变量同名的变量,
    # 则全局变量会暂时失效,而且又是在局部变量声明之前打印的,
    # 所以找不到改变量,会报错

    gb = 10
    print("fun1:" + str(gb))

fun1()
print("main:" + str(gb))

#使用global关键字修改全局变量

def fun2():
    global gb
    gb = 10
    print("fun2:" + str(gb))

fun2()
print("main:" + str(gb))
