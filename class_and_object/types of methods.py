class college:

    mandotary_marks = 50
    college_name = "GIT"

# we already discussed about namespace
    def __init__(self,marks1,marks2):
        self.marks1 = marks1
        self.marks2 = marks2

    @classmethod
    def get_School_name(cls):
        """
        if you want to work with a class variable which are common for each object we have to use cls keyword instead of using self keyword
        use decorator for not get this error .. TypeError: get_School_name() missing 1 required positional argument: 'cls'
        :return:
        """
        return cls.college_name
    @staticmethod
    def College_info():
        """
        we use static method where we are not concerned about instance and class method
        use decorator for define this is a static method
        :return:
        """
        print(f'college name : {college.get_School_name()}, Jaipur')

s1 = college(45,46)
s2 = college(42,47)

print(f'student 1 got {s1.marks1} and {s1.marks2} out of {college.mandotary_marks} and college name is : {college.get_School_name()}')
college.College_info()