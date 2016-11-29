import os
#import os.path  #引入os模块即可,os.path是属于os的
import time     #时间模块
file_path = 'e:'+ os.sep + 'a' + os.sep + 'b' + os.sep + 'abc.txt'
print(file_path)
print(os.path.basename(file_path))
print(os.path.dirname(file_path))

#将路径切成一个元组
path = (file_dir, file_name) = os.path.split(file_path)
print(path)

#分离文件名与扩展名
path = os.path.splitext(file_path)
print(path) #('e:\\a\\b\\abc', '.txt')

#得到文件信息
file_path = os.curdir + os.sep + '文件系统模块os.py'
try:
    print(os.path.getsize(file_path))#大小(字节)
    print(time.localtime(os.path.getatime(file_path)))#最近访问时间access
    print(time.localtime(os.path.getctime(file_path)))#创建时间create
    print(time.localtime(os.path.getmtime(file_path)))#最近修改时间modify
except FileNotFoundError as reason:
    print('文件不存在' + str(reason))

#判断文件是否存在
if os.path.exists(file_path):
    print('文件存在')
else:
    print('文件不存在')

#判断路径是否为绝对路径
if os.path.isabs(file_path):
    print('绝对路径')
else:
    print('不是绝对路径')

#判断是否为目录
if os.path.isdir('c:' + os.sep):
    print('目录')
else:
    print('不是目录')

#判断是否为文件
if os.path.isfile(file_path):
    print('文件')
else:
    print('不是文件')

#判断是否为一个连接(快捷方式)(失败,不知为何)
os.chdir('C:'+ os.sep +'Users'+ os.sep +'JamesXia'+ os.sep +'Desktop')
print(os.getcwd())
print(os.listdir(os.getcwd()))
if os.path.islink(os.getcwd()+ os.sep +'OS X 10.10.lnk'):
    print('是一个快捷方式')
else:
    print('不是一个快捷方式')
#判断是否为挂载点,windows则为盘符
os.chdir('E:' + os.sep)
##print(os.getcwd())
if os.path.ismount(os.curdir):
    print('挂载点')
else:
    print('不是挂载点')

#判断是否为同一个文件(判断快捷方式失败)
file1 = os.getcwd() + os.sep + '软件安装包'
os.chdir('C:'+ os.sep +'Users'+ os.sep +'JamesXia'+ os.sep +'Desktop')
file2 = os.getcwd() + os.sep + '软件安装包.lnk'
if os.path.samefile(file1, file2):
    print('同一个文件')
else:
    print('不是同一个文件')
