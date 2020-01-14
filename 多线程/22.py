import multiprocessing
from time import sleep, ctime

def consumer(input_q):
    print("Into consumer: ", ctime())
    while True:
        # 处理项
        item = input_q.get()
        print("pull", item, "out of q") # 此处替换为有用的工作
        input_q.task_done() # 发出信号通知任务完成
    # 此句未执行，以为q.join() 收到四个task_done信号后，主线程启动
    # 未等到执行print此语句
    print("Out of consumer: ", ctime())

def producer(sequeue, output_q):
    print("Into producer:", ctime())
    for item in sequeue:
        output_q.put(item)
        print("put", item, "into q")
    print("Out of producer: ", ctime())

if __name__ == '__main__':
    q = multiprocessing.JoinableQueue()

    t = multiprocessing.Process(target=consumer, args=(q,))
    t.daemon = True
    t.start()
    # 生成多个项，sequence代表要发送个消费者的项序列
    #
    sequeue = [1, 2, 3, 4]
    producer(sequeue, q)
    # 等待所有项被处理
    t.join()

