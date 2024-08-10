from abc import *

class bank:
    @abstractmethod
    def pin(self):
        pass

    def ac(self):
        print("I Will Create Account In SBI")

class sbi(bank):
    def pin(self):
        print('My pin is "Ashutoshpatil@india143"')

s=sbi()
s.pin()
s.ac()    
 


