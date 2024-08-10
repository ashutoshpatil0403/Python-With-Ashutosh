#PRIVATE METHOD===============================================================================================
# HERE WE ARE LEARNING PRIVATE,PUBLIC AND PROTECTED KEYWORD 
class mobile:
    def __init__(self,mname,password):
        self.mname=mname
        self.__password=password
#Accessing the private variable inside the class by using instance method
    #def access(self):
        #print(self.mname,self.__password)    

m=mobile("Iphone","@123%876$ashu")      
print(m._mobile__password)   # Mangling Method 

# PROTECTED METHOD ============================================================================================

class emp:
    def __init__(self):
        self._id=1

class student(emp):
    def __init__(self,name):
        super().__init__()
        self.name=name

    def dis(self):
        print(self._id,self.name)

s=student("Ashutosh")
s.dis()