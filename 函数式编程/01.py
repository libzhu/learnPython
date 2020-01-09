# coding=utf-8

# '小'函数距离
def printA():
    print("AAAAAA")

printA()

# lambda 表达式的用法
# 1、以lambda开头
# 2、紧跟一定的参数（如果有的话）
# 3、参数后面用冒号和表达式隔开
# 4、只是一个表达式，所以，没有return

# 计算一个数字的100倍
# 因为就是一个表达式， 所以没有return
stm = lambda x: 100 * x
# 使用时跟函数调用一模一样
s = stm(89)
print(s)

# 多参数
stm2 = lambda x, y, z: x + y*10 + z*100
print(stm2(4, 5, 6))

# - 高阶函数
# - 把函数作为参数使用的函数，叫高阶函数
# 变量可以赋值
a = 100
b = a

# 函数名就是一个变量
def funcA():
    print("In funcA")

# 函数名称是变量
# funcB 和 funcA 只是名称不一样而已
# 既然函数名称是变量，则可以被当成参数出入另一个函数
funcB = funcA
funcB()


# 高阶函数举例
def funcC(n):
    return n * 100

def funcD(n):
    return funcC(n) * 3

print(funcD(9))

# 写一个高阶函数
def funcF(n, f):
    return f(n) * 3
print(funcF(9, funcC))


# 系统高阶函数map
# 原意就是映射，即把集合或列表中的元素，每一个元素都按照一定规则进行操作，生成
# 一个新的列表或集合

# map 举例
# 有一个列表， 想对列表的每一个元素乘以10，并得到新的列表
l1 = [i for i in range(10)]
print(l1)
l2 = []
for i in l1:
    l2.append(i * 10)

print(l2)

# 利用map实现
def mulTen(n):
    return n * 10

l3 = map(mulTen, l1)
# map类型是一个可迭代的结构， 所以可以使用for遍历
print(type(l3))
for i in l3:
    print(i)

help(map)

# - reduce 函数
# - 原意就是归并，缩减
# - 把一个可迭代对象归并成一个结果
# - 对于作为参数的函数，必须由两个参数和一个返回值
# - reduce 需要导入functools包
# reduce([1,2,3,4,5]) = f(f(f(f(1,2), 3), 4), 5)
from functools import reduce

# 定义一个操作函数
def myAdd(x, y):
    return x + y

rst = reduce(myAdd, [1, 2, 3, 4, 5, 6])
print(rst)

# 定义一个相减函数
def myReduce(x, y):
    return x - y

ryt = reduce(myReduce, [6, 5, 4, 3, 2, 1])
print(ryt)


printA()
# filter 案例
# 对于一个列表，对其过滤偶数组成一个新的列表

# 需要定义一个过滤函数

def isEven(a):
    return a % 2 == 0

l = [2, 3, 44, 55, 66, 43, 5, 665, 446, 665]

rst = filter(isEven, l)
# 返回的filter内容是一个可迭代对象
print(type(rst))
print(rst)
print([i for i in rst])

printA()

# 排序案例 1
al = sorted(l, reverse=True) # 倒叙排列
print(al)
printA()
# 排序案例 2
a = [-55, -44, 55, 66, -77, 88, 100]
# 按照绝对值进行排序
# abs 是要求绝对值的意思
# 即按照绝对值的倒叙排列
al = sorted(a, key=abs, reverse=True)
print(al)

# sorted 案例
astr = ["Adfd", "adfd", "jjjdjdj", "hhhkjn", "eeeeer"]
str1 = sorted(astr)
print(str1)

str2 = sorted(astr, key=str.lower)
print(str2)


