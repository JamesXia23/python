def hanoi(n, x, y, z):  #演示汉诺塔的求解过程(x:源,y:辅助,z:目的)
    if(n == 1):
        print(x + "-->" + z)
    else:
        hanoi(n-1, x, z, y)     #将n-1个盘子从x移动到y(借助z)
        print(x + "-->" + z)    #将第n个盘子从x移动到z
        hanoi(n-1, y, x, z)     #将n-1个盘子从y移动到z(借助x)

n = int(input("请输入汉诺塔问题的规模:"))
hanoi(n, "X", "Y", "Z")
