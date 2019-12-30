# coding=utf-8
class Student():
    name = "dana"
    age = 18

    # 注意say的写法， 参数第一个一般约定为self
    # 实例方法
    def say(self):
        self.name = "aaaaa"
        self.age = 16
        print("my name is {}, and my age is {}".format(self.name, self.age))

yueyue =  Student()
yueyue.say()

print("*" * 100)

class Teacher():
    name = "dana"
    age = 19

    def say(self):
        self.name = "yueyue"
        self.age = 19
        print("my name is {}, may age is {}".format(self.name, self.age))

    # 声明一个 类方法
    # 访问当前类中的成员变量
    @staticmethod
    def sayAgain():
        print("hello {}".format(__class__.name))

# 实例方法的调用
t = Teacher()
t.say()

# 类方法的调用
Teacher.sayAgain()
print("*" * 100)

# Python 鸭子模型
class A():
    age = "xiaoyue"
    name = 19

    # 构造函数
    def __init__(self):
        self.name = "aaaaa"
        self.age = 200

    def say(self):
        print(self.name)
        print(self.age)

class B():
    name = "bbbb"
    age = 90

a = A()
# 此时，系统默认会把a作为第一个参数传入函数
a.say()

# 此时，self被A 代替
A.say(a)

# 同样可以用A 作为参数传入
A.say(A)

# 此时，传入的参数是类实例B 因为B具有name 和 age 所以不会报错
A.say(B)

# 以上代码 利用了鸭子模型