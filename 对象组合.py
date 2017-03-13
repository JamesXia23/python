class Fish:

    def __init__(self, num):
        self.num = num


class Tutle:

    def __init__(self, num):
        self.num = num


class Pool:

    def __init__(self, fish_num, tutle_num):
        self.fish = Fish(fish_num)  # 一定要记得加self,不然相当于在函数中定义了一个局部变量,出了函数就无效了
        self.tutle = Tutle(tutle_num)

    def show_pool(self):
        print('水池里面有鱼 %d 条, 有乌龟 %d 只' % (self.fish.num, self.tutle.num))

pool = Pool(3, 4)
pool.show_pool()

print(pool.__dict__)  # 会以字典的形式列出变量的空间
# {'tutle': <__main__.Tutle object at 0x0353ABD0>,
# 'fish': <__main__.Fish object at 0x0353ABB0>}
print(Pool.__dict__)
# {'__init__': <function Pool.__init__ at 0x018D8DB0>,
# '__dict__': <attribute '__dict__' of 'Pool' objects>,
# 'show_pool': <function Pool.show_pool at 0x018D8D68>,
# '__weakref__': <attribute '__weakref__' of 'Pool' objects>,
# '__module__': '__main__', '__doc__': None}
