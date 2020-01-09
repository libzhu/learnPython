# coding=utf-8

# 使用时先导入
import calendar

# calendar：获取一年是日历字符串
# 参数
# w = 每个日期之间的间隔字符数
# l = 每周所占用的行数
# c = 每月之间 的间隔数

cal = calendar.calendar(2020)
print(cal)

cal = calendar.calendar(2020, l=0, c=5)
print(cal)

# isleap: 判断是否是闰年
isLeap = calendar.isleap(2020)
print(isLeap)

# leapdays: 获取指定年份之间的闰年的个数
print(calendar.leapdays(2010, 2020))

# month () 获取某个月的日历字符串
# 格式 calendar.monthon(年，月)
# 返回值：月日历的字符串
print(calendar.month(2020, 1))

# monthrange() 获取一个月是周几开始和天数
# 格式：calendar.monthrange(年，月)
# 返回值：元组（周几开始，总天数）
# 注意：周默认（0 - 6）表示周一到周天

w,t = calendar.monthrange(2020, 1)
print(w)
print(t)

# monthcalendar() 返回一个月每天的矩阵列表
# 格式：calendar.monthcalendar(年，月)
# 返回值：二级表
# 注意：矩阵中没有天数用0表示
m = calendar.monthcalendar(2020, 1)
print(m)

# 直接打印一年日历
y = calendar.prcal(2020)
print(y)

m = calendar.prmonth(2020, 2)
print(m)

# weekday() 后去周几
# 格式 calendar.weekday(年，月，日)
# 返回值：周几对应的数字
w = calendar.weekday(2020, 1, 2)
print(w) # 0-6 代表周一到周天

