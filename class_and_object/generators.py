def iter():

    list = [1,3,5,7,9]
    yield list[0]
    yield list[1], list[2]


it = iter()
print(it.__next__())
for i in iter():
    print(i)


