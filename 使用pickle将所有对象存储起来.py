import pickle

list1 = [123, 3.122, 'xia', (123, 'hei')]
print(list1)
#存对象
pickle_file = open('list1.pkl', 'wb')   #注意模式一定要为wb
pickle.dump(list1, pickle_file)
pickle_file.close() #记得文件要关闭,不然数据还在缓冲区中

#读对象
pickle_file = open('list1.pkl', 'rb')
list2 = pickle.load(pickle_file)
print(list2)
