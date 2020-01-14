# coding=utf-8

# 打开文件，用写的方式
# r表示后面字符串内容不需要转义
# f 句柄
# f = open(r"test01.txt", "w")
# 文件打开后必须关闭
# f.close()

# 此案例说明，以写的方式打开文件，如果文件没有，则创建文件

# with 语句案例

with open(r"test01.txt", "r") as f:
    pass
    # 下面语句开始对文件f进行操作
    # 在这里不需要使用close关闭文件

# with 案例
with open(r"test01.txt", "r") as f:
    # 按行读取内容
    strline = f.readline()
    # 此结构保证能够完整的读取文件结构
    while strline:
        print(strline)
        strline = f.readline()

# list 能打开的文件 作为参数， 吧文件内容每一行作为一个元素

with open(r"test01.txt", "r") as f:
    l = list(f)
    for line in l:
        print(line)
print("*" * 100)
# read 是按字符读取文件内容
# 允许输入参数读取几个字符， 如果没有指定，当前位置读取到结尾
# 否侧， 从当前位置读取指定个数
with open(r"test01.txt", "r") as f:
    # 不指定个数参数
    strChar = f.read()
    print(len(strChar))
    print(strChar)

print("*" * 100)
with open(r"test01.txt", "r") as f:


    strChar = f.read(6)
    print(len(strChar))
    print(strChar)


print("*" * 100)

import time
with open(r"test01.txt", "r") as f:
    strChar = f.read(1)
    while strChar:
        print(strChar)
        time.sleep(1)
        strChar = f.read(1)

# seek(offset, from)
# - 移动文件的读取位置
# - from的取值范围
#     - 0：从文件头开始偏移
#     - 1：从文件当前位置开始偏移
#     - 2：从文件末尾开始偏移
# - 移动的单位是字节（byte）
# - 一个汉字有若干个字节组成


# seek 案例
# 打开文件后， 从第五个字节开始读取

with open(r"test01.txt", "r") as f:
    # seek 移动单位是字节byte
    f.seek(6, 0)
    strChar = f.read()
    print(strChar)


# 关于读取文件的练习
# 打开文件，三个字符一组读出内容，然后显示在屏幕上
# 每读取一次， 休息一秒钟

# 让程序暂停， 可以使用time sleep
with open(r"test01.txt", "r") as f:
    strChar = f.read(3)
    while strChar:
        print(strChar)
        #sleep 参数单位是秒
        time.sleep(1)
        strChar = f.read(3)


# tell 函数： 用来显示文件读写指针的当前位子
with open(r"test01.txt", "r") as f:
    strChar = f.read(3)
    pos = f.tell()

    while strChar:
        print(pos)
        print(strChar)

        strChar = f.read(3)
        pos = f.tell()

# 一下结果说明
# tell 的返回数字单位是byte
# read 是以字符为单位的

# 9
# 床前明
# 16
# 月光
#
# 25
# 疑似地
# 32
# 上霜
#
# 41
# 举头望
# 48
# 明月
#
# 57
# 低头思
# 63
# 故乡
