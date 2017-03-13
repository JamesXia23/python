class Person:
    name = ''    #外部定义的都是作为类变量,相当于其他语言中的static
    age = 0

    def __init__(self, name, age): #self,每一个成员方法第一个参数必须是self,只需要在定义的时候写，函数调用的时候不用写
                        #init相当于构造函数
        self.name = name    #在实例中定义了同名的self.name覆盖了类对象的name
        self.age = 20    
        self.height = 1.9   #这个是在实例对象中定义的变量

    def show_info(self):    #记得所有实例方法第一个参数都是self
        print('姓名:%s, 身高:%f, 年龄:%d' % (self.name, self.height, self.age))

    def class_method():     #类方法第一个参数就不用是self
        print('I love you')

p = Person('xia', 20)
p.show_info()
Person.class_method()

class Man(Person):
    def __init__(self, name, age):#当要重写父类的方法时，可以使用super关键字，避免父类方法被覆盖
        super().__init__(name, age)
        self.sex = 'man'
    def show_info(self):
        super().show_info()
        print("性别:%s" % self.sex)
man = Man('xiajing', 20)
man.show_info()
#序列,也是类
class Mylist(list):
    pass

l = Mylist()
l.append(3)
l.insert(0, 1)
l.append(0)
l.sort()
print(l)

#可以多重继承
class Fish:
    def swim(self):
        print('我会游泳')

class FishMan(Person, Fish):
    pass

fish_man = FishMan('jing', 22)
fish_man.show_info()
fish_man.swim()

#伪私有
class Test:
    __p = 10    #加入__将变量改名

##Test.__p
##真正变量名 ._类名__变量名

print(Test._Test__p)
