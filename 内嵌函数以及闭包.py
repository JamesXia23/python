#内嵌函数(函数内部再定义函数)
def fun1():
    print("fun1被执行")
    def fun2():
        print('fun2被执行')
    fun2()

fun1()

#闭包
#一个内部函数访问到外部的内容时,该函数称为闭包
def outer(x):
    def inner(y):
        return x * y
    return inner

i = outer(5)    #此时i为一个函数变量inner
print(i(6))     #相当于调用了inner,结果为30

#如果在一个内部函数中想要修改外部变量
#那就意味着必须重新定义这个变量,
#则外部变量就会被屏蔽
#def outer2():
#    x = 5
#    def inner2():
#        x *= x
#        return x  #重新定义了x,相当于x1 = x2 * x3
                #(按道理先执行x2*x3,都是全局变量,但是由于定义了x1,所以全局x被屏蔽,而又是先执行x2*x3,在定义x1之前,所以找不到x2和x3的定义,会报错)
#    return inner2() #这里返回的不是函数变量,而是函数返回值

#outer2()

#解决办法,将x设置为nonlocal变量,跟全局变量global关键字作用类似
def outer3():
    x = 5
    def inner3():
        nonlocal x
        x *= x
        return x  
    return inner3() 

outer3()
