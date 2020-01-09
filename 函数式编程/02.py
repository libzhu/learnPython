# coding=utf-8

# 定义一个普通函数
def myF(a):
    print("In myF")
    return None


a = myF(8)
print(a)

# 函数作为返回值返回，被返回的函数在函数体中定义
def myF2():
    def myF3():
        print("In myF3")
        return 3

    return myF3

f = myF2()
print(f)
print(type(f))

# 调用
t = f()
print(t)

# 返回函数的例子
# args:参数列表'

def myF4( *args):
    def myF5():
        rst = 0
        for i in args:
            rst += i

        return rst
    return myF5

f5 = myF4(1, 2, 3, 4, 5, 89, 99)
# f5 的调用方式
print(f5())

f6 = myF4(1, 2, 3, 4, 5)
# f5 的调用方式
print(f6())

# 闭包（closure）
# 当一个函数在内部定义函数，并且内部的函数使用外部函数的参数或局部变量，内部函数被当成返回值放回时，
# 相关参数和值保存在返回的函数中 我们称 这种结果为闭包。
# 上面例子 为典型的闭包结构

# 闭包常见的坑
def count():
    # 定义一个列表，列表中存放的是定义的函数
    fs = []
    for i in range(1, 4):

        # 定义一个函数f
        def f():
            return i * i

        fs.append(f)
    return fs

t = count()
print(type(t))
print(t)
# 期望 1， 4， 9
# 结果：9， 9， 9
f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# 上述出现的问题
# 造成上述原因：返回函数引用变量1，i 并非立即执行，而是等到 三个函数都返回时统一使用，
# 此时 i 已经变成3了，最终调用的时候都返回 3 * 3
# 返回闭包时，返回函数不能引用任何循环变量

# 解决办法
def count2():
    # 定义一个列表，列表中存放的是定义的函数

    def otherf(i):
        def f():
            return i * i

        return f

    fs = []
    for i in range(1, 4):
        fs.append(otherf(i))
    return fs

f3, f4, f5 = count2()
print(f3())
print(f4())
print(f5())

# 装饰器
def hello():
    print("hello world")
hello()
f = hello
f()

print(f.__name__)

# 对hello功能进行扩张，每次打印hello之前打印当前系统
# 而实现这个功能又不能改动现有代码
# ==> 使用装饰器

# 对 hello函数进行功能扩展， 每次执行hello时打印当前时间
import time

def pritTime(f):
    def wrapper(*args, **kwargs):
        print("Time: {0}".format(time.ctime()))
        return f(*args, **kwargs)
    return wrapper

# 上面定义了装饰器， 使用的时后需要用到@，此符号是Python的语法糖
@pritTime
def hello():
    print("hello world, hello beijing")

hello()

# 装饰器的好处，一旦定义，则可以装饰任意函数
# 一旦被器装饰，则把函数的功能直接添加到定义的功能上
@pritTime
def hello2():
    print("今天好搞笑")
    print("有很多好玩的")

hello2()

# 偏函数
# 把字符串转化成十进制数字
p = int("12345")
print(p)
# 八进制的字符串12345， 表示成十进制的数字
t = int("12345", base=8)
print(t)

def int16(x, base=16):
    return int(x, base)

h = int16("12345")
print(h)

import functools
# 实现上面int16的功能
otherInt16 = functools.partial(int, base=16)
o = otherInt16("12345")
print(o)



