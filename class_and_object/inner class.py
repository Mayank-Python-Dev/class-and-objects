class flat:

    def __init__(self,bathroom,hall,kitchen):
        """
        if you want to define inner class in outside class flat ..
        first you have to create an object for that inner class using self keyword you can create an object of inner class
        and now you can implement that object in outside class flat

        :param bathroom:
        :param hall:
        :param kitchen:
        """
        self.bathroom = bathroom
        self.hall = hall
        self.kitchen = kitchen
        self.mem = self.members()

    def show(self):
        print(f'this flat has {self.bathroom} bathroom, {self.hall} hall, and {self.kitchen} kitchen')
        self.mem.show()

    class members:

        def __init__(self):
            self.name = "Mayank"
            self.age = 26

        def show(self):
            print(f'{self.name} , {self.age}')

f1 = flat(2,1,1)
f1.show()