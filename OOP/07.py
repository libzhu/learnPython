# coding=utf-8


def printFunc():
    print("*" * 100)
    return None

# 函数名可以当变量使用
def sayHello(name):
    print("{0} 你好， 来一份牛排吗？".format(name))

sayHello("月月")

# 函数名当变量使用直接
yueyue = sayHello
yueyue("yueyue")

# 自己组装类 示例 1
class A():
    pass

def say(self):
    print("Saying......")

class B():
    def say(self):
        print("B:Say...........")

A.say = say

a = A()
a.say()

say(9)

b = B()
b.say()

printFunc()

# 自己组装类 示例 2
from types import MethodType

class C():
    pass

def sayHello(self):
    print("Say..........")


c = C()
c.sayHello = MethodType(sayHello, C)
c.sayHello()

# help(MethodType)

printFunc()

# 利用type造一个类 示例3
def talk(self):
    print("talking.......")

def sing(self):
    print("sing..........")
# 用 type 来创建一个类
T = type("Aname",(object, ), {"class_sing":sing, "class_talk":talk})
print(T.__dict__)

printFunc()
# 然后可以正常使用类一样
t = T()
print(dir(t))
t.class_sing()
t.class_talk()

printFunc()

# 元类
# 元类写法是固定的 必须继承自type
# 元类一般命名为MetaClass 结尾
class StudentMetaClass(type):
    # 注意一下写法
    def __new__(cls, name, bases, attrs):

        # 自己的业务处理
        print("我是元类")
        attrs["id"] = "000000"
        attrs["addr"] = "湖北武汉"

        return type.__new__(cls, name, bases, attrs)

class Teacher(object, metaclass=StudentMetaClass):
    pass

t = Teacher()
print(t.id)
print(t.addr)