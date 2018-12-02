old_file_name = input('请输入要打开的文件:');
old_file = open(old_file_name, 'r', encoding='UTF-8');

position = old_file_name.rfind('.')
new_file_name = old_file_name[:position] + '[复件]' + old_file_name[position:]
new_file = open(new_file_name, 'w', encoding='UTF-8')
new_line = old_file.readline()
# 读法1：但一个大文件，而且只有一行时会爆炸
# while(new_line != ''):
#     new_file.write(new_line)
#     new_line = old_file.readline()
buf_len = 2048
buf = old_file.read(buf_len)
while len(buf) > 0:
    new_file.write(buf)
    buf = old_file.read(buf_len)
old_file.close()
new_file.close()

