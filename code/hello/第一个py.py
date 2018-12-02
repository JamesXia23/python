import random   #引入模块
secret = random.randint(1,10)
print("-------------第一个py-------------")

while 1:
    temp = input("猜数字:")
    guess = int(temp)
    if guess == secret:
        print("你真懂我")   #print自动换行
        break
    else:
        if guess > secret:
            print("大了")
        else:
            print("小了")
        
print("游戏结束")
print("1234",end="")    #使用空串代替换行，禁止换行
print("游戏结束")
print("hello","world",sep=" ")  #自定义输出之间的分隔符
print("i'm a student")  #在字符串中输入单引号

#dir(__builtins__) #列出所有内置函数(小写开头的),直接在控制台输入
#help(input) #函数说明
 
