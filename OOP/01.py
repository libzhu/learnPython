# coding=utf-8
'''
定义一个学生类， 用来用来形容学生
'''
# 定义一个空的类
class Student():
    # 一个空类，pass代表直接跳过
    pass

# 定义一个对象
mingyue = Student()


# 定义一个类， 用来描述Python的学生类
class PythonStudent():
    # 用None 给不确定的值赋值
    name = None
    age = 18
    course = "Python"

    def doHomework(self):
        print ("{} 在做作业".format(self.name))

        # 推荐在 函数末尾使用return 语句
        return  None

# 实例化一个叫yueyue的学生，是个具体的人
yueyue = PythonStudent()
print (yueyue.name)
print (yueyue.age)

print(yueyue.__dict__)
print(PythonStudent.__dict__)

for i in PythonStudent.__dict__:
    print(PythonStudent.__dict__[i])


# 默认吧 yueyue 传入self
yueyue.doHomework()

print("*" * 100)

# 声明一个类

"""
下面案例说明：
类的属性和类的实例属性，在不对类的实例属性赋值情况下，它们的属性 指向同一变量
"""

class A():
    name = "dana"
    age = 18

print(A.name)
print(A.age)

print(A.__dict__)
print(id(A.name))
print(id(A.age))
print("*" * 100)

# 实例化 一个对象
a = A()
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
print(a.__dict__)
print("*" * 100)

a.name = "小明"
a.age = 19

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))
print(a.__dict__)
print("*" * 100)



