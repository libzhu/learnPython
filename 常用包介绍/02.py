# coding=utf8

# 导入时间模块
import time

# timezone 当前时区和UTC时间相差的秒数
print(time.timezone)

# 得到时间错
print(time.time())

# localtime 得到当前的时间结构
# 可以通过点号操作获取元素的属性
t = time.localtime()
print(t)
print("{0}年{1}月{2}日 {3}:{4}:{5}".format(t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec))

# asctime() 返回元组的正常字符串化之后的格式时间
t = time.localtime()
tt = time.asctime(t)
print(type(tt))
print(tt)

# ctime:获取字符串化的当前时间
t = time.ctime()
print(t)

# mktime() 使用时间元组获取对应的时间戳
# 格式 time.mktime()
# 返回值：浮点数时间戳
lt = time.localtime()
ts = time.mktime(lt)
print(ts)
# clock 获取cpu时间
print(time.clock())

# sleep 使程序进入睡眠 n秒后继续
for i in range(10):
    print(i)
    time.sleep(1)

# strftime: 将时间元组转化为自定义的字符串格式
t = time.localtime()
ft = time.strftime("%Y年%m月%d日 %H:%M", t)
print(ft)
