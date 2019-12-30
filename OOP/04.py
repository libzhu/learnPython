# coding=utf-8
import math

def printFunc():
    print("*" * 100)
    return None


# 属性案例
class Dog():
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # 如果不想修改代码
        self.setName(name)


    def intro(self):
        print("Hai, my name is {}".format(self.name))

    def setName(self, name):
        self.name = name.upper()

xiaohua = Dog("xiaohua", 1)
xiaohua.intro()
print(xiaohua.name, xiaohua.age)

xiaohei = Dog("xiaohei", 2)
xiaohei.intro()
print(xiaohei.name, xiaohei.age)

printFunc()

# property 案例
# 定义一个 Person 类 具有name age属性
# 对于输入的英文name 我们都希望用大写方式保存
# 对于年龄， 我们希望统一用整数保存

class Person():

    def fget(self):
        return self._name * 2

    def fset(self, name):
        self._name = name.upper()

    def fdel(self):
        self._name = "NoName"

    name = property(fget, fset, fdel, "对name操作")

p1 = Person()
p1.name = "xiaoran"
print(p1.name)

printFunc()

age = input("请输入年龄")
print("年龄是：{}".format(age))

class Student():
    def fget(self):
        return self._age

    # 引入 match 数学库 向下取整 floor， 向上取整 ceil
    def fset(self, age):
        self._age = math.floor(age)

    def fdel(self):
        self._age = 0

    age = property(fget, fset, fdel, "对年进行操作")


s = Student()
s.age = float(age)
print("学生的年龄：{}".format(s.age))

printFunc()

# 类的内容函数
print(Student.__dict__)
print(Student.__name__)
print(Student.__bases__)
print(Student.__doc__)

printFunc()


# 魔法函数

# init 举例
class A():
    def __init__(self, name):
        print("哈哈， 我被调用了")

a = A("dana")

printFunc()

# __call__ 举例
class B():
    def __init__(self, name = 9):
        print("我被调用了")

    def __call__(self, *args, **kwargs):
        print("我又被调用了")


b = B()
b()

printFunc()

# str 举例
class C():
    def __init__(self):
        print("我被创建了")

    def __str__(self):
        return("xxxxxxxxx")

c = C()
print(c)

printFunc()

# getattr 举例
class D():
    name = "NoName"
    age = 18
    # 访问一个不存在的属性时 触发
    def __getattr__(self, item):
        print("没有找到：{}".format(item))
        return None

d = D()
print(d.name)
print(d.test)

printFunc()

# __setattr__ 案例
class Person():
    def __init__(self):
        pass

    def __setattr__(self, key, value):
        print("设置属性：{0}".format(key))
        # 下面语句会导致死循环
        # self.key = value
        #此种情况，为了避免死循环，规定统一调用父类
        super(Person, self).__setattr__(key, value)

p = Person()
p.age = 18

printFunc()


# __gt__ 案例 比较大小 自动触发

class Student():
    def __init__(self, name):
        self._name = name

    def __gt__(self, other):
        print("哈哈 {0} 会比 {1} 大吗".format(self._name, other._name))
        return self._name > other._name

stu1 = Student("one")
stu2 = Student("two")
print(stu1 > stu2)
