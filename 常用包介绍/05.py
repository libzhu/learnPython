# coding=utf-8

# shutil 模块

import shutil, os, time

mydir = os.getcwd()
print(mydir)

ls = os.listdir()
print(ls)

# 在当前目录下执行一个dana.haha的文件夹
rst = os.system("touch dana.haha")# 在当前目录下执行一个dana.haha的文件夹


# copy() 复制文件
# 格式：shutil.copy(来源路径， 目标路径)
# 返回值：目标路径
# 拷贝的同时可以给文件重命名
rst = shutil.copy("/Users/vteam/Desktop/app项目/IOS重要练习资料/LearnPython/learnPython/常用包介绍/dana.haha", "/Users/vteam/Desktop/app项目/IOS重要练习资料/LearnPython/learnPython/常用包介绍/dana/haha.haha")
print(rst)

# copy2() 复制文件
# 格式：shutil.copy2(来源路径， 目标路径)
# 返回值：目标路径
# 拷贝的同时可以给文件重命名
# 注意：copy 和 copy2 的唯一区别在于copy2 复制文件时尽量保留员数据

# copyfile() 将一个文件中的内容复制到另外一个文件中
# 格式：shutil.copyfile(源路径， 目标路径)
# 返回值：无
rst = shutil.copyfile("dana.haha", "haha.haha")
print(rst)

# move() 移动文件/文件夹
# 格式：shutil.move(源路径，目标路径)
# 返回值：目标路径
dst = shutil.move("dana.haha", "/Users/vteam/Desktop/app项目/IOS重要练习资料/LearnPython/learnPython/常用包介绍/dana")
print(dst)

time.sleep(4)

# 归档和压缩
# 归档：把多个文件或文件夹合并到一个文件当中
# 压缩：用算法把多个文件或文件夹无损或者有损合并到一个文件当中

# make_archive() 归档操作
# 格式：shutil.maek_archive('归档之后的目录和文件名', '后缀','需要归档的文件夹')
# 返回值：归档之后的地址

pst = shutil.make_archive("/Users/vteam/Desktop/app项目/IOS重要练习资料/LearnPython/learnPython/常用包介绍/tianyi/", "zip", "/Users/vteam/Desktop/app项目/IOS重要练习资料/LearnPython/learnPython/常用包介绍/dana")
print(pst)

# unpack_archive() 解包操作
# 格式 shutil.unpack_archive("归档文件地址"， 解包后的地址)
# 返回值：解包后的地址

time.sleep(5)
# zip - 压缩包
# 某块名称：zipfile
import zipfile
zf = zipfile.ZipFile("tianyi.zip")


