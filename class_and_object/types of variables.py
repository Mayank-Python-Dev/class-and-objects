class apartment:  # what is namespace  = it is an area where you create or store object/variables

    ff = "full furnished"
    # this ff is called static or class variable ,, if we try to change the value of it.. it will change the value of each object
    # because this class variable is common for each object
    # this is called class namespace
    def __init__(self):
         """
         all self keyword here is a instance variable .. why instance variable ?
         because we can change the value it for each and every object ..
         thats why we call instance variable
         this is called instance namespace
         """
         self.hall = 1
         self.bathroom = 2
         self.kitchen = 1

a1 = apartment()
a2 = apartment()
a2.bathroom = 3
apartment.ff = "semi-furnished"


print(f'This apartment has {a1.hall} hall, {a1.bathroom} bathrooms and {a1.kitchen} kitchen and it is a {apartment.ff} flat')
print(f'This apartment has {a2.hall} hall, {a2.bathroom} bathrooms and {a2.kitchen} kitchen and it is a {apartment.ff} flat')