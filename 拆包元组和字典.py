def test(a, b, c=33, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

A = (1, 2, 3)
B = {"d": 1, "e": 2}
test(4, 5, 6, A, B) # 没写*的话，A和B都装入args
test(4, 5, 6, *A, **B) # 拆包，将A拆出来赋值给args，B拆出来赋值给kwargs
