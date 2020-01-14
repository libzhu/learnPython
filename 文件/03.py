# coding=utf-8

# 持久化 pickle
# - 序列化（持久化， 落地),把程序运行中的信息保存在磁盘上
# - 反序列化：序列号的逆过程
# - pickle：Python提供的序列化模块
# - pickle.dump: 序列化
# - pickle.load: 反序列化

# 序列化案例
import pickle

age = 19
with open(r"test01.txt", "wb") as f:
    pickle.dump(age, f)

# 反序列化
with open(r"test01.txt", "rb") as f:
    a = pickle.load(f)
    print(a)

# 序列化案例
a = [19, "liudana", "i love beijing", [19, 18]]
with open(r"test02.txt", "wb") as f:
    pickle.dump(a, f)

with open(r"test02.txt", "rb") as f:
    a = pickle.load(f)
    print(a)

# 持久化 - shelve
# - 持久化工具
# - 类似字典，用kv对保存数据，存取方式和字典也类似
# - open close

import shelve

# 打开文件
# shv相当于一个字典
shv = shelve.open(r"shv")
shv["one"] = 1
shv["two"] = 2
shv["three"] = 3

shv.close()

# shelve 读取案例
shv = shelve.open(r"shv")
try:
    print(shv["one"])
    print(shv["two"])
    print(shv["three2"])

except Exception as e:
    print("未知错误")
finally:
    shv.close()


# - shelve特性
#     - 不支持多个应用并行写入
#         - 为了解决这个问题，open的时候可以使用flag=r
#     - 写回问题
#         - shelve：特殊情况下不会等待持久化对象进行任何修改
#         - 解决办法：强制写回，writeback = True

shv = shelve.open(r"shv")
try:
    shv["one"] = {"enis":1, "zwei":2, "drei":3}
finally:
    shv.close()

shv = shelve.open(r"shv")
try:
    one = shv["one"]
    print(one)
finally:
    shv.close()

# shelve 忘记写回，需要强制写回
shv = shelve.open(r"shv")
try:
    k1 = shv["one"]
    print(k1)
    k1["enis"] = 100
finally:
    shv.close()

shv = shelve.open(r"shv")
try:
    k1 = shv["one"]
    print(k1)

finally:
    shv.close()

print("*" * 100)

# shelve 忘记写回，需要强制写回 writeback=true
shv = shelve.open(r"shv", writeback=True)
try:
    k1 = shv["one"]
    print(k1)
    k1["enis"] = 100
finally:
    shv.close()

shv = shelve.open(r"shv")
try:
    k1 = shv["one"]
    print(k1)
finally:
    shv.close()






