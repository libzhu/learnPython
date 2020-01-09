# coding=utf-8

print("hello world")
import os


# getcwd() 获取当前的工作目录
# 格式：os.getcwd()
# 返回值：当前工作目录的字符串
# 当前工作目录就是程序进行文件相关操作，默认操作文件目录

mydir = os.getcwd()
print(mydir)


# chdir() 改变当前的工作目录
# change directory
# 格式：os.chdir(路径)
# 返回值：无
os.chdir("/Users/vteam/Desktop/app项目/IOS重要练习资料/LearnPython")
mydir = os.getcwd()
print(mydir)

os.chdir("/Users/vteam/Desktop/app项目/IOS重要练习资料/LearnPython/learnPython/常用包介绍")
mydir = os.getcwd()
print(mydir)

# listdir() 获取一个目录中所有的子目录和文件的名称列表
# 格式 os.listdir(路径)
# 返回值：所有子目录和文件名称的列表

ld = os.listdir()
print(ld)
for i in ld:
    if i == "dana":
        # 路径拼接 （为保证代码通用性，及在 Windows / macos 中能同时使用，不能用"\" 或 "/" 拼接）
        path = os.path.join(mydir,i)
        print(path)
        # os.rmdir("{0}/{1}".format(mydir,i)) # 删除当前dana路径
        # os.removedirs("{0}".format(i)) # 删除当前dana路径
        os.removedirs(path)

ld = os.listdir()
print(ld)

print("*" * 100)


import time
time.sleep(2)

# makedir() 递归创建文件夹
# 格式：os.makedirs(递归路径)
# 返回值：无
# 递归路径：多个文件夹层包含的路径就是递归
rst = os.makedirs("dana")


ld = os.listdir()
print(ld)  # 目录列表中存在dana文件夹


# system() 执行系统shell命令
# 格式：os.system(系统命令)
# 返回值：打开一个shell或终端界面

ls = os.system("ls")
print(ls)


# 在当前目录下执行一个dana.haha的文件夹
rst = os.system("touch dana.haha")

# getenv() 获取指定的系统环境变量值
# 格式：os.getenv("环境变量名")
# 返回值：指定环境变量名对应的值
pth = os.getenv("PATH")
print(pth)

# exit() 退出当前程序
# 格式 exit()
# 返回值：无


# 值部分
# os.curdir: 当前目录
# os.pardir: 父目录
# os.sep: 当前系统的路径分隔符  windows: "\"  masos: "/"
# os.linesep: 当前系统的换行符 window: "\r\n", macos:"\n"
# os.name: 当前系统的名称 windows:nt  mac: posix

print("*" * 100)

print(os.curdir)
print(os.pardir)

print(os.sep)
print(os.linesep)

print(os.name)


# 在路径的相关操作中，不要手动拼写地址，因为手动拼写的地址不具备可移植性
path = "/Users/vteam" + "/" + "dana"
print(path)


import os.path as op
# os.path 模块， 跟路径相关的模块
# abspath() 将路劲转化为绝对路径
# 格式：os.path.abspath("路径")
# 返回值：路径的绝对路径形式
absp = op.abspath(".")
print(absp)

# basename() 获取路径中的文件名部分
# 格式：os.path.basename(路径)
# 返回值：文件名字符串
bn = op.basename(absp)
print(bn)

# join() 将多个路径拼接合并成一个路径
# 格式：os.path.join(路径1， 路径2)
# 返回值：组合之后的新字符串路径

mydir = os.getcwd()
print(mydir)

ls = os.listdir()
print(ls)

path = ''
for i in ls:
    if i == "dana.haha":
        path = os.path.join(mydir, i)
        print(path)

print("*" * 100)

# split() 将路径切割成文件部分和当前文件部分
# 格式：os.path.split(路径)
# 返回值：路径和文件名组成的元组
p, f = op.split(path)
print(p)
print(f)

# isdir() 检查是否是目录
# 格式 os.path.isdir(路径)
# 返回值：布尔值
isml = os.path.isdir(p)
print(isml)

# exists() 检查文件目录是否存在
# 格式 os.path.exists(路径)
# 返回值：布尔值
e = os.path.exists(p)
print(e)


