#filter函数,遍历序列,筛选出符合规则的值,返回一个序列:
    #参数1:筛选规则函数,默认为None,此时会将序列中所有值为true的筛选出来
    #参数2:筛选序列
list1 = list(range(10))   #range:产生一个0-9的序列
print(list1)

print(list(filter(lambda x : x % 2, list1))) #筛选出模2为1的,也就是奇数
