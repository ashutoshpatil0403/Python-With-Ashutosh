# CONSTRUCTORS
class person:
    def __init__(self) : # constructor are used to initialize the object
        print("Hello World")

p1=person()
p2=person()
p3=person()

# types of constructors: 1) default constructor 2) parametarized constructor

# 1) Default Constructor=======================================================
class emp:
    def __init__(self) :
        self.id=1
        self.name="Ashutosh Patil"

    def display(self):
        print(self.id)
        print(self.name)

a=emp()
a.display()            

# 2) Parametarised Constructor===================================================

class employee:
    def __init__(self,id,sal):
        self.id=id
        self.sal=sal
    def display(self):
        print(self.id) 
        print(self.sal) 

e=employee(1,"Rajadhiraj Yogiraj Chhatrpati Shivaji Maharaj KI jai KI jai KI jai")

e.display()

#constuctor overloading

class empp:
    def __init__(self):
        
        print("Hello")
    def __init__ (self,a):
         
        print("good") 
    def __init__ (self,a,b):
        print("Morning")
#b=empp()
#b=empp(2)
b=empp(1,2)   
