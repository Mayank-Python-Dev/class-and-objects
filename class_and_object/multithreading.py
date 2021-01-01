import threading
import time


class A:

    def __init__(self):
        self.array = [2,3,4,5]

    def calc_square(self):
        print("Starting our calc_square function")
        x = self.array
        for i in x:
            time.sleep(0.2)
            print(f'Square :',i * i)

class B:

    def __init__(self):
        self.array = [2,3,4,5]

    def calc_cube(self):
        print("Starting our calc_cube function")
        x = self.array
        for i in x:
            time.sleep(0.2)
            print(f'Cube :',i * i * i)
c1 = A()
c2 = B()
c1 = threading.Thread(target=c1.calc_square())
c2 = threading.Thread(target=c2.calc_cube())

c1.start()
c2.start()

c1.join()
c2.join()

end_t = time.time()
print(f"it is taking:",end_t)

