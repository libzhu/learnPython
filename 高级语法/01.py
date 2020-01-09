# coding=utf-8

# zip 案例
l1 = [1, 2, 3, 4, 5]
l2 = [11, 22, 33, 44, 55]
z = zip(l1, l2)
print(type(z))
print(z)
for i in z:
    print(i)


l3 = ["wangwang", "mingye", "yyt"]
l4 = [89, 33, 88]
z1 = zip(l3, l4)
print([i for i in z1])

# enumerate
# 跟zip功能比较像
# 对可迭代对象的每一个元素，配上一个索引

# enumerate
l5 = [11, 88, 99, 90, 30]
em = enumerate(l5)
l6 = [i for i in  em]
print(l6)

em = enumerate(l5, start=100)
l7 = [i for i in em]
print(l7)


# collections 模块
# nametuple
#     - tuple 类型
#     - 是一个可命名的tuple

import collections
# 点 坐标 x, y
Point = collections.namedtuple("Point", ["x", "y"])
p = Point(11, 22)
print(p.x)
print(p[0])

# 坐标x，y 半径50
Circle = collections.namedtuple("Circle", ["x", "y", "r"])
c = Circle(100, 200, 50)
print(type(c))

# 检查namedtuple 到底属于谁的子类
iszl = isinstance(c, tuple)
print(iszl)

# dequeue
# - 比较方便的解决频繁删除插入带来的效率
from collections import deque
q = deque([1, 3, 4, 5, 8, 7])
q.append(9)
print(q)

# 前面插入
q.appendleft(10)
print(q)

# 按下标删除
q.__delitem__(3)
print(q)

# 删除元素
q.remove(3)
print(q)

# defaultdict
# - 当直接读取dict 不存在的属性时，直接返回默认值
d1 = {"one":1, "two":2, "three":3}
print(d1["one"])
# print(d1["four"]) # four不存在，会报错

from collections import defaultdict
# lambda 表达式，直接返回字符串
func = lambda : "dana"
d2 = defaultdict(func)

d2["one"] = 1
d2["two"] = 2
print(d2["one"])
print(d2["four"]) # 调用上面定义的函数

# Counter
# - 统计字符串个数
from collections import Counter
c = Counter("abcdefgadcddddffffff")
print(type(c))
print(c)

s = ["liudana", "love", "love", "love", "love"]
c1 = Counter(s)
for i in c1:
    print(i)
    print(c1[i])
print(c1)




