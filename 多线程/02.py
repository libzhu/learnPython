# 利用Time生成两个 函数
# 顺序调用
# 计算总的时间

import time
import _thread as thread
def loop1():
    # ctime 得到当前时间
    print("Start loop 1 at: ", time.ctime())
    time.sleep(4)
    print("End loop 1 at: ", time.ctime())

def loop2():
    print("Start loop 2 at: ", time.ctime())
    time.sleep(2)
    print("End loop 2 at: ", time.ctime())


def main():
    print("Starting at: ", time.ctime())

    thread.start_new(loop1, ())
    thread.start_new(loop2, ())

    print("All done at: ", time.ctime())

if __name__ == '__main__':
    main()
    # 死等
    while True:
        time.sleep(1)