class duck:

    def go(self):
        print("duck can swim")
        print("duck can fly")
        print("duck can walk")

class bird:

    """
    if a bird can swim like duck , walk like duck , and fly like duck .. it is a duck
    if you are passing a bird_name and it has a go method .. that is called duck typing
    """

    def run(self,bird_name):
        bird_name.go()

# we are creating one more class to understand the concept of duck typing

bird_name = duck()  # you can give a duck()
b1 = bird()
b1.run(bird_name)
