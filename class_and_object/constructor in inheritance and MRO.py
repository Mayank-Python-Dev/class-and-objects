class A:
    """
    __init__ is a constructor of class A ..
    it will automatically get called when you create an object of this class
    Same concept is use for other class
    """
    def __init__(self):
        print(f'in A init')

    def method1(self):
        print(f'Hello method1 is working')

class B: # class b(A): = TypeError: Cannot create a consistent method resolution
    """
    so every class has a constructor
    what if i use inheritance concept in class C ?
    will it print constructor of class ?

    """
    def __init__(self):
        print(f'in B init')

    def method2(self):
        print(f'hello method2 is working')

class C(A,B):  # suppose class C has only one parent class(B)  it will first check itself if a constructor is present in their class it will print that first
    """
    MRO = Method resolution order : it always start from left to right .. let me show you the example in here

    """
    def __init__(self):
        super().__init__()   # If you want to fetch the constructor of class A .. you can use super() keyword or method
        print(f'in C init')

    def method3(self):
        print(f'hello method3 is working')

c1 = C()


