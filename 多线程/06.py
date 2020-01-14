# coding=utf-8

# 非守护线程

import time
import threading

def fun():
    print("start fun")
    time.sleep(4)
    print("End fun")

print("Main Thread")

t1 = threading.Thread(target=fun, args=())
t1.start()

time.sleep(2)
print("Main thread end")