# coding=utf-8

# raise 案例
# 自己定义异常
# 需要注意：自定义异常必须是系统异常的子类
class DanaValueError(ValueError):
    pass
try:
    print("我爱北京天安门")
    print(123213.22)

    # 手动引发异常
    # 注意语法：raise ErrorClassName
    # raise ValueError
    raise DanaValueError
    print("还没有完")
except NameError as e:
    print("NameError")
except DanaValueError as e:
    print("DanaValueError")
except ValueError as e:
    print("ValueError")
except Exception as e:
    print("有异常")
finally:
    print("我肯定会执行的")


