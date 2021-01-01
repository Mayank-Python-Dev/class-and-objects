# Method overloading
class A:

    def sum(self,a=None,b=None,c=None):
        """
        method overloading means you have same function name in same class itself but different no.of params
        In python we don't have a method overloading concept ..
        but we can use some condition(if-else) to define the method overloading ..
        :param a:
        :param b:
        :param c:
        :return:
        """
        if a!=None and b!=None and c!=None:
            x = a + b + c
        elif a!=None and b!=None:
            x = a + b
        else:
            x = a

        return x

a1 = A()
print(a1.sum(5,6,9))

# Method Overriding

class A:

    def show(self):
        """
        method overriding means you have same function and same no.of params in different class'
        in python we don't have a method overriding concept
        but we can use inheritance concept to define the method overriding
        :return:
        """
        print("In A Show")

# class B(A):
#     pass
class B(A):

    def show(self):
        """
        In this sceario first it will check that is show method is available in my class if it is present
        it will print that if it is available .. otherwise it will go to class A
        because class b(child class) inherits all the features of class A(parent class)
        :return:print(next(it))
        """
        print("in B Show")
        
a1 = B()
a1.show()