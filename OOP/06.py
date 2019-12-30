# coding=utf-8

def printFunc():
    print("*" * 100)
    return None

#  变量的三种用法
class A():

    def __init__(self, name):
        self.name = "haha"
        self.age = 18

a = A("dana")
# 属性的三种操作
#1、赋值
#2、读取
#3、删除
print(a.name)
a.name = "dana"
print(a.name)
del a.name
# print(a.name)

printFunc()

# 类属性 property
# 对变量除了普通的三种操作，还想增加一些附加的操作，那么可以通过property完成
class B():
    def __init__(self):
        self.name = "haha"
        self.age = 18

    # 此功能，是对类变量进行读取操作的时候执行的函数功能
    def fget(self):
        print("我被读取了")
        return self.name

    # 对变量进行写操作的时候执行的功能
    def fset(self, name):
        print("我被写入了")
        self.name = "天逸公司" + name
    # 删除的时候需要进行的操作
    def fdel(self):
        pass

    # property 第四个参数顺序是固定的
    # 1、第一个参数是读取的时候的调用的函数
    # 2、第二个参数代表写入的时候调用的函数
    # 3、第三个参数是删除时候调用的函数
    name2 = property(fget, fset, fdel, "这是一个property例子")


b = B()
print(b.name)

printFunc()

# 抽象
class Animel():

    def sayHello(self):
        pass

class Dog(Animel):
    pass


class Person(Animel):
    pass

# 以下仅为抽象类定义示例
# 抽象类的实现
# import abc
# # 声明一个类并指定当前类的原类
# class Human(metaclass=abc.ABCMeta):
#
#     # 定义一个抽象方法
#     @abc.abstractmethod
#     del smoking(self):
#         pass
#
# #   # 定义一个类抽象方法
#     @abc.abstractclassmethod
#     del drink():
#         pass
#
#     # 定义一个静态抽象方法
#     @abc.abstractstaticmethod
#     def play()
#         pass
#
#     del sleep(self):
#         print("sleep....")