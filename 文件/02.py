# coding=utf-8

# - w: 写方式打开，会覆盖以前的内容
# - write(str)
# 把字符串写入文件
# - writelines(str): 把字符串按行写入
# - 区别
# - write参数只能是字符串
# - writelines
# 参数可以是字符串， 也可以是字符序列

# write 案例
# 1、向文件追加一句诗

# a 代表追加方式打开
with open(r"test02.txt", "a") as f:
    #
    f.write("生活不止有眼前的苟且, \n还有远方的苟且")

# 可以直接写入，且用writelines
# writelines 表示写入很多行，
# a 代表追加的方式打开
with open(r"test04.txt", "a") as f:
    f.writelines("窗前明月光")
    f.writelines("疑似地上霜")

l = ["I", "Love", "Beijing"]
with open(r"test03.txt", "w") as f:
    f.writelines(l)