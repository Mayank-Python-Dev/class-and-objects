from time import sleep
from threading import *

class hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)

class hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)


t1 = hello()
t2 = hi()

t1.start() # doing this you can create a threads
sleep(0.2)
t2.start() # we are calling start method because in Thread we have run method
# so in total we have 3 thread 1.Main thread 2.t1 thread 3.t2 thread

t1.join()  # join() = let t1 and t2 complete the execution
t2.join()  # join() = let t1 and t2 complete the execution

# after join .. main thread will do their work to printing bye
print("bye")