def file_read():

    f = open("exception_handling.txt",'r')
    print(f.read())
    f.close()
file_read()

def copy_image():

    f = open("Motivation.jpg","rb")
    f1 = open("New_image.JPG","wb")
    for i in f:
        f1.write(i)
    f1.close()

# print(f.closed) will tell you the file is closed or not