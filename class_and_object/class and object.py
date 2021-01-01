# types of variable  = 1.instance variable 2.class variable or static variable
class Car:
    wheels = 4  #instance variable

    def __init__(self,car,mil):
        self.car = car # static variable
        self.mil = mil # static variable

    def printing(self):
        print(f"car is : {self.car} and mileage is : {self.mil} and wheels is = {Car.wheels} ")  # here car of wheels is common for each object

car1  = Car("BMW",12)
car2  = Car("AUDI",15)
car1.printing()
car2.printing()


class A:
    Id = 1

    def __init__(self):
        self.name = "mayank"
        self.age = 26

a1 = A()
a2 = A()
a2.name = "Rashi"
a2.age = 24

print(f'ID : {a1.Id} My name is : {a1.name} , age = {a1.age}')
print(f'ID : {a2.Id} My name is : {a2.name} , age = {a2.age}')