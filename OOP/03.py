# coding=utf-8

# 类的封装
class Person():
    # name 是公有的成员
    name = "xiaoming"
    # __age 是私有成员 前面用两个下划线__
    __age = 19 # 年龄不方便透露

p = Person()
# name是公有的
print(p.name)

# age 是私有的  无法访问
# print(p.age)

print("*" * 100)
# name mangling 技术
print(Person.__dict__)
p.Person_age = 100
print(p.Person_age)

print("*" * 100)

# 类的继承
# 在Python中 任何一个类都有一个共同的父类叫 object
class Person2():
    name = "noName"
    age = 0
    __score = 0 # 考试成绩密码，只有自己知道 私有的
    _petname = "sec" # 小名，是保护的， 子类可用， 但不能公用

    def sleep(self):
        print("sleeping...")

    def work(self):
        print("make some money")

# 父类写在括号里
class Teacher(Person2):
    teacher_id = "9527"
    name = "dana"
    def makeTest(self):
        print("老师能够考试")

    # 扩充父类的功能，只需要调用相应的函数
    def work(self):
        # 调用父类的两种方法 类名 或 super()
        # Person2.work(self) # self  子类可以冒充父类填充 但父类不能冒充子类
        super().work()
        self.makeTest()

t = Teacher()
print("姓名：{}".format(t.name))
t.sleep()

# 子类访问父类私有属性报错
# print(t.__score)

# 访问受保护的属性
print(t._petname)
print(t.teacher_id)
t.makeTest()

# 子类与父类 成员变量名称相同时优先使用子类
print(t.name)

t.work()

print("*" * 100)

# 构造函数的概念
class Dog():
    # __init__  就是构造函数
    # 每次实例化的时候，第一个被自动调用
    # 因为主要工作是初始化 ，所以得名
    def __init__(self):
        print("I am init in dog")

kaka = Dog()

print("*" * 100)

# 继承中的构造函数
class Animel():
    def __init__(self):
        print("初始化 animel")

class PaxingAni(Animel):
    def __init__(self):
        print("Paxing .....")

class Dog(PaxingAni):
    def __init__(self):
        print("初始化dog")
# 实例化时 自动调用了 Dog 的构造函数
# 因为找到了构造函数，则不再向上查找父类的构造函数
titi = Dog()

# 猫 没有写构造函数
class Cat(PaxingAni):
    pass
# 此时应该自动调用构造函数， 因为cat 没有构造函数，所有向上查找是否有父类构造函数，并调用
c = Cat()


print("*" * 100)

# 继承中的构造函数 - 2
class Animel():
    def __init__(self):
        print("初始化 animel")

class PaxingAni(Animel):
    def __init__(self, name):
        print("Paxing .....:{}".format(name))

class Dog(PaxingAni):
    def __init__(self):
        print("初始化dog")
# 实例化时 自动调用了 Dog 的构造函数
# 因为找到了构造函数，则不再向上查找父类的构造函数
titi = Dog()

# 猫 没有写构造函数
class Cat(PaxingAni):
    pass
'''
此时应该自动调用构造函数， 因为cat 没有构造函数，所有向上查找是否有父类构造函数，并调用 父类构造函数中有两个参数 self、 name
所以需要传入 name 参数
'''
c = Cat("小花")


print("*" * 100)
# 多继承的
class A():
    pass

class B(A):
    pass

class C(B, A):
    pass

# 多继承关系混乱问题
# class D(C, A, B):
#     pass
class D(C):
    pass

print(A.__mro__)
print(B.__mro__)
print(C.__mro__)
print(D.__mro__)