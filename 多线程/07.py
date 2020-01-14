# coding=utf-8

# 守护线程

import time
import threading

def fun():
    print("start fun")
    time.sleep(4)
    print("End fun")

print("Main Thread")

t1 = threading.Thread(target=fun, args=())
# 守护线程的方法：必须在启动自谦设置，否则无效
t1.daemon = True
t1.start()

time.sleep(2)
print("Main thread end")