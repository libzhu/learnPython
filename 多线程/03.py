
# 利用Time生成两个 函数
# 顺序调用
# 计算总的时间

import time
import _thread as thread

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
    # 启动多线程的意思是 用多个线程执行某个函数
    # 启动多线程函数 start_new thread
    # 参数两个：一个是函数运行的函数名，第二个是函数的参数作为元组使用
    # 注意：如果函数只有一个参数，需要参数后有一个逗号
    thread.start_new(loop1, ("王大拿",))
    thread.start_new(loop2, ("王小鹏", "王晓静"))

    print("All done at: ", time.ctime())

if __name__ == '__main__':
    main()
    # 死等
    # while 语句
    # 以为启动多线程后程序就作为主线程运行
    # 如果主线程执行完毕，则子线程可能也要终止
    while True:
        time.sleep(1)