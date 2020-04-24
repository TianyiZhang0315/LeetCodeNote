#1195多线程交替打印
import threading 
class FizzBuzz:
    def __init__(self, n: int):
        self.n = n+1
        self.Fizz=threading.Semaphore(0)
        self.Fizzbuzz=threading.Semaphore(0)
        self.Buzz=threading.Semaphore(0)
        self.Num=threading.Semaphore(1)

    # printFizz() outputs "fizz"
    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        for i in range(1,self.n):
            if i%3 ==0 and i%5 !=0:
                self.Fizz.acquire()
                printFizz()
                self.Num.release()

    # printBuzz() outputs "buzz"
    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        for i in range(1,self.n):
            if i%3 !=0 and i%5==0:
                self.Buzz.acquire()
                printBuzz()
                self.Num.release()
    	  	

    # printFizzBuzz() outputs "fizzbuzz"
    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        for i in range(1,self.n):
            if i%3==0 and i%5==0:
                self.Fizzbuzz.acquire()
                printFizzBuzz()
                self.Num.release()
    	
    # printNumber(x) outputs "x", where x is an integer.
    def number(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1,self.n):
            self.Num.acquire()
            if i%3==0 and i%5==0:
                self.Fizzbuzz.release()
            elif i%3==0:
                self.Fizz.release()
            elif i%5==0:
                self.Buzz.release()
            else:
                printNumber(i)
                self.Num.release()

#1114按序打印
from threading import Lock

class Foo:
    def __init__(self):
        self.firstJobDone = Lock()
        self.secondJobDone = Lock()
        self.firstJobDone.acquire()
        self.secondJobDone.acquire()

    def first(self, printFirst: 'Callable[[], None]') -> None:
        # printFirst() outputs "first".
        printFirst()
        # Notify the thread that is waiting for the first job to be done.
        self.firstJobDone.release()

    def second(self, printSecond: 'Callable[[], None]') -> None:
        # Wait for the first job to be done
        with self.firstJobDone:#这里是在等待first()释放锁，锁被释放，在此处获取后就执行下一行
            # printSecond() outputs "second".
            printSecond()
            # Notify the thread that is waiting for the second job to be done.
            self.secondJobDone.release()

    def third(self, printThird: 'Callable[[], None]') -> None:

        # Wait for the second job to be done.
        with self.secondJobDone:
            # printThird() outputs "third".
            printThird()
def print2():
    print(2)

def print1():
    print(1)

def print3():
    print(3)

if __name__ == "__main__":
    d = []
    item = Foo()
    d.append(threading.Thread(target = item.first,args = (print1,)))
    d.append(threading.Thread(target = item.third,args = (print3,)))
    d.append(threading.Thread(target = item.second,args = (print2,)))
    for t in d:
        t.start()
    for t in d:
        t.join(1)
##python3 说明一下，with lock的意思是自动加锁与解锁，等价于if lock.acquire(): ..... lock.release()。
##
##所以以下代码也是可以的
##
##if self.secondJobDone.acquire():
##     printThird()
##     self.secondJobDone.release()


#进程
##from multiprocessing import Process
##import os
##
### 子进程要执行的代码
##def run_proc(name):
##    print('Run child process %s (%s)...' % (name, os.getpid()))
##
##if __name__=='__main__':
##    print('Parent process %s.' % os.getpid())
##    p = Process(target=run_proc, args=('test',))
##    print('Child process will start.')
##    p.start()
##    p.join()
##    print('Child process end.')
                
#信号和线程                
##import threading
##import time
##def fun(semaphore, num):
##    # 获得信号量，信号量减一
##    semaphore.acquire()
##    print("Thread %d is running." % num)
##    print()
##    #time.sleep(3)
##    # 释放信号量，信号量加一
##    semaphore.release()
##    print("current",threading.current_thread().name)
##    print()
##if __name__=='__main__':
##    # 初始化信号量，数量为2
##    semaphore = threading.Semaphore(2)
##
##    # 运行4个线程
##    threads = []
##    for num in range(4):
##        t = threading.Thread(target=fun, args=(semaphore, num),name = str(num))
##        threads.append(t)
##        #print(threading.current_thread().name)
##    
##    for t in threads:
##        t.start()
##    for t in threads:
##        t.join(1)
                
#多进程和进程池
##from multiprocessing import Pool
##import os, time, random
##
##def long_time_task(name):
##    print('Run task %s (%s)...' % (name, os.getpid()))
##    start = time.time()
##    time.sleep(random.random() * 3)
##    end = time.time()
##    print('Task %s runs %0.2f seconds.' % (name, (end - start)))
##
##if __name__=='__main__':
##    print('Parent process %s.' % os.getpid())
##    p = Pool(4)
##    for i in range(5):
##        p.apply_async(long_time_task, args=(i,))
##    print('Waiting for all subprocesses done...')
##    p.close()
##    p.join()
##    print('All subprocesses done.')



