#文件的打开模式:
    #r:只读(默认)
    #w:写入,会覆盖已存在的文件
    #x:如果文件已存在会爆出异常
    #a:如果文件存在,则在末尾最加
    #b:以二进制模式打开
    #t:以文本模式打开(默认)
    #+;可读写模式,可添加到其他模式中使用
    #U:通用换行符支持

# r、w、a：只读(文件不存在报错)、只写(覆盖)、只追加(存在追加，不存在重新创建)
# r+、w+、a+：读写(文件不存在报错)、读写(覆盖)、读写(存在追加，不存在重新创建)

file = open('三元操作符.py')
print(file) #<_io.TextIOWrapper name='三元操作符.py' mode='r' encoding='cp936'>
#读取文件,read()
#print(file.read())  #不指定参数则读至文件末尾
print(file.read(10))    #指定则读取默认字符个
print(file.tell())  #返回当前指针指向的位置(字节数)
file.seek(0, 0) #第一个参数offset,代表偏移字节数
                #第二个参数代表从何处开始偏移0:文件起始,1:当前位置,2:文件末尾
print(file.tell())

print(file.readline())  #一次读一行

print(list(file))   #可以将文件字节转化为列表,按换行来分

file.seek(0, 0)
for each_line in file:  #可以直接遍历文件,也是按换行来分
    #print(each_line)    #不过这样换行符也会读出来
    print(each_line, end="")

#写文件
write_file = open('file_write.txt', 'w')
write_file.write('Hello,World\n')  #将字符串写入文件
#print(help(file))
#write_file.write(write_file.newlines())
write_file.write('你好python\n')
write_file.writelines(('nihao\n',str(123)+'\n','hehhe')) #传入一个序列,会将序列依次写入文件(不带换行)
                                                #而且序列中的元素必须为字符串,
write_file.close()
