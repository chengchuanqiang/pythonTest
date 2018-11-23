import threading
import time

exitFlag = 0


class MyThread(threading.Thread):
    def __init__(self, threadId, name, counter):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.counter = counter

    def run(self):
        print('开始线程：' + self.name)
        self.printTime(self.name, self.counter, 5)
        print('退出线程：' + self.name)

    def printTime(self, threadName, delay, counter):
        while counter:
            if exitFlag:
                threadName.exit()
            time.sleep(delay)
            print('%s : %s' % (threadName, time.ctime(time.time())))
            counter -= 1


# 创建新的线程
thread1 = MyThread(1, 'Thread-1', 1)
thread2 = MyThread(2, 'Thread-2', 2)

# 开始新的线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('退出主线程')
