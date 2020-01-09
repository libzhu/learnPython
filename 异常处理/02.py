# coding=utf-8

help(ZeroDivisionError)


# 简单异常案例
try:
    num = int(input("请输入一个数字"))
    rst = 100 / num
    print("计算结果：{0}".format(rst))
# 多种错误的情况
# 捕获异常后，把异常实例化， 出错信息会在实例里
# 注意一下写法
# 以下语句捕获ZeroDivisionError异常并实例化e
# 把越容易出现的错误越往前放
# 越是父类的异常，越往后放

# 在处理错误的时候，一旦拦截到某一个异常，则不再继续往下查看，
# 直接进行下一个代码，即有finally 则执行finally语句块，否则执行下一个打的语句
except ZeroDivisionError as e:
    print("你输入的什么玩意啊")
    print(e)
    # print("*" * 100)
    # for estr in dir(e):
    #     print(estr)
    # exit 退出程序的意思


except NameError as e:
    print("名字错误")
    print(e)

except AttributeError as e:
    print("属性错误")
    print(e)

#Exception 常规错误的基类
# Exception 应该写在最后一个 except
except Exception as e:
    print("我也不知道什么错误了")
    print(e)


print("hello world")


