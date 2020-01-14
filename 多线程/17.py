import threading
import time

def func():
    print("I am running......")
    time.sleep(4)
    print("I an done")

if __name__ == '__main__':
    # 多少秒之后执行某函数或方法
    t = threading.Timer(6, func)
    t.start()

    i = 0
    while True:
        print("{0}***************".format(i))
        time.sleep(3)
        i += 1
