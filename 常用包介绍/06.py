# coding=utf-8

# random

import random

# random() 获取0-1之间的随机小数
# 格式random.random()
# 返回值：随机0-1之间的小数
print(random.random())

# 0 - 100 之间的随机整数
z = int(random.random() * 100)
print(z)

# choice() 返回数列中的某个值
# 格式：random.choice(序列)
# 返回某个值
l = [str(i)+"hahha" for i in range(10)]
print(l)
rst = random.choice(l)
print(rst)

# shuffle() 随机打乱列表
# random.shuffle(列表)
# 返回值：打乱顺序之后的列表
l1 = [i for i in range(10)]
print(l1)

random.shuffle(l1)
print(l1)

help(random.shuffle)

# randint(a,b) 返回一个a和b 之间的整数 包含a和b （randint 是个特例，其他一般为左包括，右不包括）
print(random.randint(0, 100))
help(random.randint)