# 多线程同时访问共有属性示例
# 期望值 sum = 0

import threading
sum = 0
loopSum = 1000000

look = threading.Lock()
def myAdd():
    global sum, loopSum
    for i in range(1, loopSum):
        # 上锁，申请令牌
        look.acquire()
        sum += 1
        # 释放锁
        look.release()

def myMinu():
    global sum, loopSum
    for i in range(1, loopSum):
        look.acquire()
        sum -=1
        look.release()


if __name__ == '__main__':
    print("Start........ ", sum)
    t1 = threading.Thread(target=myAdd, args=())
    t1.start()

    t2 = threading.Thread(target=myMinu, args=())
    t2.start()

    t1.join()
    t2.join()

    print("Done........ ", sum)