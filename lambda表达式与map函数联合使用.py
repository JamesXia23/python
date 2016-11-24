#map函数,参数和filter函数一致,返回经过映射函数映射后的序列
    #参数1:映射函数
    #参数2:被映射序列
print(list(range(10)))
print(list(map(lambda x : x * 2, range(10))))
