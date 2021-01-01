class fib:

    def fibonacci(self):

        """
    1. The yield keyword in python works like a return with the only difference is that instead of returning a value, it gives back a generator function to the caller.
    2. A generator is a special type of iterator that, once used, will not be available again. The values are not stored in memory and are only available when called.
    3. The values from the generator can be read using for-in, list() and next() method.
    4. The main difference between yield and return is that yield returns back a generator function to the caller and return gives a single value to the caller.
    5. Yield does not store any of the values in memory, and the advantage is that it is helpful when the data size is big, as none of the values are stored in memory.
    6. The performance is better if the yield keyword is used in comparison to return for large data size.
        :return:
        """
        self.a = 0
        self.b = 1
        while True:
            yield self.a
            self.a,self.b = self.b,self.a+self.b

f1 = fib()
fib1 = f1.fibonacci()
print(fib1)
for i in fib1:
    if i > 100:
        break
    print(i)
# """

#
# """