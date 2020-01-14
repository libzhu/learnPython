# 可重入锁案例

import threading

# mutex = threading.Lock()
# RLock 可重入锁
mutex = threading.RLock()
num = 0

class MyThread(threading.Thread):
    def run(self):
        global num
        if mutex.acquire():
            num += 1
            msg = self.name + " set num to " + str(num)
            print(msg)
            mutex.acquire()
            mutex.release()
            mutex.release()

def testTh():
    for i in range(5):
        t = MyThread()
        t.start()

if __name__ == '__main__':
    testTh()

