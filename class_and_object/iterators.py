list = [1,2,3,4,5]

it = iter(list)
print(it) # it will give me object and allow me to use next function to fetch the values one by one

print(it.__next__())

print(next(it))

print(dir(list))

print(dir(it))

#reversed order iterations
list1 = [1,2,3,4,5]

ite = reversed(list1)

print(next(ite))
print(ite.__next__())



