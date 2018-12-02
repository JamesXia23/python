import random
import os
secret = random.randint(1, 10)
print(secret)

print('==============')

#模块常量
#os.curdir:指代当前文件夹 .
#os.pardir:指代父目录    ..
#os.sep:指代文件分隔符   //或者\
#os.linesep:行终止符(win:\r\n,linux:\n)
#os.name:当前系统名称:(posix:unix, nt:windows, mac:macOS, )
print(os.getcwd())
os.chdir('E:' + os.sep)
print(os.getcwd())
#print(os.listdir('E:\软件安装包'))   #列出文件夹下所有文件,以列表返回
print(os.listdir(os.curdir))

try:
    #os.mkdir('py测试')    #创建文件夹,当存在时会抛异常
    os.makedirs('py测试'+ os.sep +'abc' + os.sep + 'ede' + os.sep + 'gfge')   #递归创建
except FileExistsError as reason:
    print('文件夹已存在')
##try:
##    os.removedirs('py测试')#递归删除目录,遇到非空会抛出异常
##    print('文件夹已删除')
##except OSError:
##    print('删除文件夹成功')

#想要递归删除文件夹,需要使用另一个模块shutil
import shutil
shutil.rmtree('py测试')   #递归删除

os.mkdir('python测试')
os.rename('python测试', 'py测试')

#运行系统命令
os.system('calc')

name = os.name
#当前系统名称
if name == 'nt':
    print('Windows')
elif name == 'posix':
    print('Unix')
elif name == 'mac':
    print("macOS")
