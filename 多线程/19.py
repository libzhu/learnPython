import multiprocessing
from time import sleep, ctime


def clock(interval):
    while True:
        print("The time is %s" % ctime())
        sleep(interval)

if __name__ == '__main__':
    # 创建一个进程
    p = multiprocessing.Process(target=clock, args=(5,))
    p.start()

    # 主线程结束：线程和进程也会结束，所以要开启死循环，保持主线程一直活着。
    while True:
        sleep(1)