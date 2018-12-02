#format有两种参数,位置参数和关键字参数

#位置参数
print("{0} {1}, i love {2}".format("james", "xia", "you"))
#关键字参数
print("{er} {hahah}, i love {fuck}".format(er='xia', hahah='jing', fuck='you'))
#位置参数可以与关键字参数共用,不过位置参数一定要在关键字参数之前

#可以用{对{进行转义
print("{{0}}".format('hhhehehe'))   #结果:{0}因为{被转义了,{0}不再是位置参数了
print("{0:.2f}{1}".format(27.26587, "GB"))

#使用格式字符
print("wo xiahuan %c" % 97)
print("%s, 今年%d岁" % ('夏靖', 20))#多个参数用元组来传递

#控制小数格式
print("%5.2f" % 27.487453)
print("%5.2e" % 27.484244)
print("%10d" % 12)
print("%-10d" % 12)#右边补空格
print("%+10d" % 5)#显示符号

#显示进制
print("%#o" % 456)  #显示8进制数
print("%#X" % 456)  #显示16进制数
