#使用with会自动帮你关闭文件
try:
    with open('sfee.txt', 'r') as f:
        for each_line in f:
            print(each_line)
except FileNotFoundError as reason:
    print('文件不存在' + str(reason))
except OSError as reason:
    print('出错了:' + str(reason))
    
