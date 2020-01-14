

# 利用Time生成两个 函数
# 顺序调用
# 计算总的时间

import time
import threading

def loop1(in1):
    # ctime 得到当前时间
    print("Start loop 1 at: ", time.ctime())
    print("我是参数：", in1)
    time.sleep(4)
    print("End loop 1 at: ", time.ctime())

def loop2(in1, in2):
    print("Start loop 2 at: ", time.ctime())
    print("我是参数一：", in1, "参数二：", in2)
    time.sleep(2)
    print("End loop 2 at: ", time.ctime())


def main():
    print("Starting at: ", time.ctime())

    # 生成threading.Thread 实例
    # 注意：如果函数只有一个参数，需要参数后有一个逗号
    t1 = threading.Thread(target=loop1, args=("王老大",))
    t1.start()

    t2 = threading.Thread(target=loop2, args=("王大鹏", "王大拿"))
    t2.start()
    print("All done at: ", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)

