class laptops:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram


    def configuration(self):
        print(f'config : {self.cpu} , {self.ram}')

    def update_config(self,l2):
        l2.cpu = 'i5'
        l2.ram = 16

    def compare(self,l2):
        if self.cpu == l2.cpu:
            return True
        else:
            print(f'they are different')


l1 = laptops('i5', 8)
l2 = laptops('ryzen', 16)

l1.update_config(l2)

l1.configuration()
l2.configuration()

if l1.compare(l2):
    print("they are same")