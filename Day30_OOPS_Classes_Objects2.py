#TYPES OF VARIABLES

# inside the constructor
class emp:
    def __init__(self,id,name) :
        self.id=id
        self.name=name

    def display(self):
        print(self.id)
        print(self.name)

a=emp(1,"ashutosh")
a1=emp(2,"ashish")
a.display()  
a1.display() 

# inside the methods 
class student:
    def display(self):
        self.id=1       # without using constructor
        self.name="Ashutosh"
        self.age=24
        print("id =",self.id)
        print("name =",self.name)
        print("age =",self.age)

s=student()
s.display()        

#  Using the object name
#we can declare and initialize instance variable value using object name


print("Hello macha")

class stu:
    def __init__(self, id, name, age):
        self.id = id    
        self.name = name
        self.age = age
    
    def display(self):
        print("id =", self.id)
        print("name =", self.name)
        print("age =", self.age)

# Creating an instance of the stu class and passing values for id, name, and age
s1 = stu(1, "Ashutosh", 23)
# Calling the display method of the instance
s1.display()


class flipcart:
    def __init__(self, pid,pname,price):
        self.pid = pid    
        self.pname = pname
        self.price = price
    def select(self):
        print("pid =", self.pid)
        print("pname =", self.pname)
        print("price =", self.price)
f= flipcart(1, "iphone",150000)
f.select ()

#==============================================================================================
class std:
    clgname="IIT Bombay"
    
s=std()
print(s.clgname) #or
print(std.clgname)

#================================================================================================

class customer:
    ifsc="SBI0302"
    def __init__(self,cname,cid,cno):
        self.cname=cname
        self.cid=cid
        self.cno=cno

    def display(self):
        print(self.cname)
        print(self.cid)
        print(self.cno)

c=customer("ashu",1,9898989898)
c.display()
print(customer.ifsc)
#print(customer.cid)  attribute error
