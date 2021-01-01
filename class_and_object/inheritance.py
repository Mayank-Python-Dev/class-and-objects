def single_inheritance():

    class A:  # super class or parent class
        def method1(self):
            print(f"Method 1 is working")

        def method2(self):
            print(f"Method 2 is working")

    class B(A):  # sub-class or child class
        def method3(self):
            print(f"Method 3 is working")

        def method4(self):
            print(f"Method 4 is working")

    b1 = B()  # with this b1 object you can use the methods of super class
    # here b1 sub-class) inheriting all the features from super class (class A)
    b1.method3()
single_inheritance()

def multi_level_inheritance():

    class A:  # super class or parent class
        def method1(self):
            print(f"Method 1 is working")

        def method2(self):
            print(f"Method 2 is working")

    class B(A):  # sub-class or child class of Class A
        def method3(self):
            print(f"Method 3 is working")

        def method4(self):
            print(f"Method 4 is working")

    class C(B): # sub-class or child class of Class B
        def method5(self):
            print(f"method 5 is working")
    c1 = C()
    c1.method1()
multi_level_inheritance()

def multiple_inheritance():

    class A:  # super class or parent class
        def method1(self):
            print(f"Method 1 is working")

        def method2(self):
            print(f"Method 2 is working")

    class B():
        def method3(self):
            print(f"Method 3 is working")

        def method4(self):
            print(f"Method 4 is working")

    class C(A,B): # sub-class of Class A and Class B
        def method5(self):
            print(f"method 5 is working")

    c1 = C()
    c1.method2()
multiple_inheritance()










