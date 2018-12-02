#基本的分支,if-else

#与循环连用,当循环正常执行完成时则调用,如果循环是使用break退出的,就不调用
num = int(input('请输入一个数:'))
if num <= 2:
    print(str(num) + '是素数')
else:
    i = 2
    while((num % i) != 0):
        if(i == num - 1):
            print(str(num) + '是素数')
            break
        i += 1
    else:
        print(str(num) + '不是素数')

#与异常处理使用,当不会发生异常时执行

try:
    num = 1 / 2
except ZeroDivisionError:
    print('除0异常')
else:
    print('正常执行')
