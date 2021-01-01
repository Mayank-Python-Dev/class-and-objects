class students:

    def __init__(self, marks):
        self.marks = marks
        self.total_marks = 500

    def __gt__(self, other):
        """
        __gt__ this is called magic methods
        normally what we do is using operators like +,-,/ for performing some operation
        but behind the scene it is calling a magic methods like __add__,__sub__,__div__ that are presented in a class like int,str,float .. which are dependent on user input like int,str,float etc
        :param other:
        :return:
        """
        if self.marks > other.marks:
            print(f'{self.marks} is the highest marks when compare to {other.marks}')
        else:
            print(f'{other.marks} is the highest marks when compare to {self.marks}')


    def __bool__(self):
        mandatory_marks = 450
        if self.marks >= mandatory_marks:
            return True
        else:
            return False

    def compare(self,other):
        if self.marks > other.marks:
            print(f'you got higher marks {self.marks} as compared to {other.marks}')
        else:
            print(f'you got higher marks {other.marks} as compared to {self.marks}')

s1 = students(440)
s2 = students(470)
s3 = students(450)
s4 = students(480)
result = students.__gt__(s2,s4)
result1 = students.__bool__(s1)
if result1 == True:
    print(f"Congratulations! you are pass ")
else:
    print(f"Sorry! try to learn more .. best wishes for your next exam :)")
s4.compare(s2)



