print(dir(str))
#和列表元组很相似
str1 = 'i lova adan'
str2 = str1[2:]
print(str2)

#将字符串第一个字符改为大写,返回一个新的字符串
str3 = str1.capitalize()
print(str3)

#将整个字符串改为小写,返回一个新的字符串
str4 = 'ASDFAG'
print(str4.lower())
str4 = str4.casefold()#与lower()功能一致,想要变大写用upper()
print(str4)
#翻转大小写
str4 = 'asdeSDGWAEGA'
print(str4.swapcase())

#用空格填充字符串,使字符串居中
str4 = str4.center(40)
print(str4)

#用空格填充字符串,使字符串左对齐
str4 = 'ASDFAG'
str4 = str4.ljust(30)
print(str4)
#右对齐可以用rjust

#检查字符串是否以某个子串结尾
str5 = 'asdgesad'
print(str5.endswith('a'))
print(str5.endswith('a', 0, len(str5) - 1))
#检查以某个子串开头用startswith()

#将tab用空格代替,默认tab是8个字符,可以用tabsize改变,返回一个新的字符串
str6 = 'james\txia\tshi\txia\tjing'
print(str6)
str6 = str6.expandtabs(tabsize=12)
print(str6)

#寻找子串,找不到返回-1
str7 = 'i love adan'
print(str7.find('love'))    #同样可以指定start,end
#从右边开始找可以使用rfind

#index,和find功能一样,不过找不到的时候会产生一个异常
#rindex从右边查

#各种判断isxxx,判断字符串是否只包含xxx
#isalnum:长度大于等于1,所有字符都是数字,或者所有字符都是字母
#isalpha:都是字母
#isdecimal:都是十进制数字
#isdigit:都是数字
#isnumeric:都是数字
#isspace:都是空格
#istitle:所有单词都是首字母大写,其余小写
#islower:都是小写
#isupper:都是大写

#将字符串作为参数字符串每个字母的分隔符
str8 = 'jamesxia'
print(str8.join('123456'))  #1jamesxia2jamesxia3jamesxia4jamesxia5jamesxia6

#去掉字符串左边的所有空格
str4 = 'ASDFAG'
str4 = str4.center(40)
print(str4)
print(str4.lstrip())

#去掉字符串右边的所有空格
str4 = 'ASDFAG'
str4 = str4.center(40)
print(str4)
print(str4.rstrip())

#去掉字符串两端的所有空格
str4 = 'ASDFAG'
str4 = str4.center(40)
print(str4)
print(str4.strip())
str4 = 'aaaaaasssssaaaaa'
print(str4.strip('a'))#如果给一个参数,那会切掉前后的参数,剩下sssss

#找到子字符串sub,将原来字符串分为三个元组
str9 = 'i love you'
tuple1 = str9.partition('ov')
print(tuple1)       #('i l', 'ov', 'e you')
#rpartition从右边找sub

#替换字符串
str10 = 'i love you you you'
print(str10.replace('you', 'me'))#默认是全部替换,replace all
print(str10.replace('you', 'her', 2))#第三个参数指定最多替换的个数

#使用translate替换字符串
str10 = 'i love you you you'
print(str10.translate(str.maketrans('ou', 'yy')))#替换的两个字符串的长度必须相等

#切割字符串(返回列表)
str11 = 'i love you you you'
print(str11.split())#默认以空格分割
print(str11.split(sep='o'))
str12 = """锄禾日当午
汗滴禾下土"""
print(str12.splitlines())

#标题化字母
str13 = 'i love you'
print(str13.title())
