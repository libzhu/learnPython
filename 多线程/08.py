
import time
import threading

def loop1():
    # ctime 得到当前时间
    print("Start loop 1 at: ", time.ctime())
    time.sleep(6)
    print("End loop 1 at: ", time.ctime())

def loop2():
    print("Start loop 2 at: ", time.ctime())
    time.sleep(1)
    print("End loop 2 at: ", time.ctime())

def loop3():
    print("Start loop 3 at: ", time.ctime())
    time.sleep(5)
    print("End loop 3 at: ", time.ctime())


def main():
    print("Starting at: ", time.ctime())

    # 生成threading.Thread 实例
    # 注意：如果函数只有一个参数，需要参数后有一个逗号
    t1 = threading.Thread(target=loop1, args=())
    t1.setName("Thread01")
    t1.start()

    t2 = threading.Thread(target=loop2, args=())
    t2.setName("Thread02")
    t2.start()

    t3 = threading.Thread(target=loop3, args=())
    t3.setName("Thread03")
    t3.start()

    time.sleep(3)
    for thr in threading.enumerate():
        print("正在运行的子线程：{0}".format(thr.getName()))
        print("正在运行的子线程数量：{0}".format(threading.activeCount()))
    # ALL done 最后执行
    print("All done at: ", time.ctime())

if __name__ == '__main__':
    main()
    while True:
        time.sleep(10)
