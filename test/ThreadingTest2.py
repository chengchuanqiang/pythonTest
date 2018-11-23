import threading


def threadFun(x, y):
    for i in range(x, y):
        print(i)


thread1 = threading.Thread(target=threadFun, args=(1, 6))
thread2 = threading.Thread(target=threadFun, args=(10, 15))

thread1.start()
thread2.start()


# 继承thread.Thread类创建线程
# 重载threading.Thread类的run方法，然后调用start()开启线程就可以了
class myThread(threading.Thread):

    def __init__(self, threadName, x, y):
        threading.Thread.__init__(self)
        self.x = x
        self.y = y
        self.threadName = threadName

    def run(self):
        for i in range(self.x, self.y):
            print(self.threadName, '   ', i)


t1 = myThread('thread-1', 1, 2)
t2 = myThread('thread-2', 10, 13)
t1.start()
t2.start()
