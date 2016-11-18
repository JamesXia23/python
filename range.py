a = range(5)    #产生0-4的range对象
b = list(a)     #将range转化为列表
for i in a:
    print(i)

for j in range(2, 10):  #产生2-9的range
    print(j)

for k in range(3, 30, 4):   #产生3到29，步进为4的数
    print(k)
