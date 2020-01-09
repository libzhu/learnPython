# coding=utf-8

# datetime提供日期和时间的运算和表示

import datetime
import time

# datetime 常见属性
# datetime.date 一个理想的日期， 提供year month day属性
dt = datetime.date(2020,1,3)
print(dt)
print(dt.year)
print(dt.month)
print(dt.day)


# datetime.time: 提供一个理想和的时间， hour minute sec microsec
from  datetime import datetime, timedelta
# 常用的方法
# today
# now
# utcnow
# fromtimestamp 从时间戳返回本地时间
dt = datetime(2020,1,3)
print(dt.today())
print(dt.now())

print(dt.fromtimestamp(time.time()))


# datetime.datetime： 提供日期和时间的组合


# datetime.timedelta：提供一个时间差，时间长度

t1 = datetime.now()
print(t1)
print(t1.strftime("%Y-%m_%d %H:%M:%S"))

# 时间间隔
td = timedelta(hours=1) #表示一个小时之后
print((t1+td).strftime("%Y-%m_%d %H:%M:%S"))


# timeit - 时间测量工具
# 测量时间运行时间间隔

def p():
    time.sleep(3.6)

t1 = time.time()
p()
print(time.time() - t1)


# 利用timeit 调用代码， 执行1000次 查看运行时间

import timeit

c = """
sum = []
for i in range(1000):
    sum.append(i)
    
"""
t1 = timeit.timeit(stmt="[i for i in range(1000)]", number=100000)

t2 = timeit.timeit(stmt=c, number=100000)

print(t1)
print(t2)

help(timeit.timeit)


# timeit 可以执行一个函数，来测量一个函数的执行时间
def doIt():
    num = 3
    for i in range(num):
        print("Repeat for {0}".format(i))

# 执行函数 重复10次
t3 = timeit.timeit(stmt=doIt, number=10)
# print(t3)

# 另外一个例子
s = """
def doIt(num):
    for i in range(num):
        print("Repeat for {0}".format(i))
"""

# num=3 是带入s 这一段小代码中的参数
t4 = timeit.timeit(stmt=s, setup=s+"num=3", number=10)
print(t4)







