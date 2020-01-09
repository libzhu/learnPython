# coding=utf-8

l = [1, 2, 3, 4]
# print(l[5]) # IndexError: list index out of range 数组越界

# 简单异常案例
try:
    num = int(input("请输入一个数字"))
    rst = 100 / num
    print("计算结果：{0}".format(rst))
    
except:
    print("你输入的什么玩意啊")
    # exit 退出程序的意思
    exit()

