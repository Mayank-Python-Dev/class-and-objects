class Car_gear :

    def __init__(self,gear_name):
        self.gear_name = gear_name
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        itr = self.index
        if self.index == len(self.gear_name):
            raise StopIteration
        self.index+=1
        return self.gear_name[itr]

ALTO = Car_gear([1, 2, 3, 4, 5, 'REVERSE'])
ite = iter(ALTO)
print(next(ALTO))
for i in ALTO:
    print(i)

class topten:

    def __init__(self,x):
        self.x = x
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        itr = self.index
        if self.index == len(self.x):
            raise StopIteration
        self.index+=1
        return self.x[itr]


nums = topten([1,2,3,4,5,6,7,8,9,10])
ite = iter(nums)
for i in nums:
    print(i)