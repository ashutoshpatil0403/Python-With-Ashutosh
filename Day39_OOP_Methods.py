# METHOD OREVRIDING=====================INHERITANCE CONCEPT CAME HERE===========================================
class amazon:
    def offer(self):
        print("Summer discount is 10%")

class flipcart(amazon):
    def offer(self):
        print("Winter discount is 25%")

f=flipcart()
f.offer()          

#EXAMPLE OF BANKING=============================================================
class sbi:
    def interest(self):
        print("Summer interest is 10%")

class boi(sbi):
    def interest(self):
        print("Winter interest is 25%")

class hdfc(sbi):
    def interest(self):
        print("Winter interest is 15%")        

b=boi()
h=hdfc()
b.interest()    
h.interest()

# CONSTRUCTOR IS SAME

class clg:
    def __init__(self,id,name):
        self.id=id
        self.name=name

class emp(clg):
    def __init__ (self,id,name,sal):
        #self.id=id
        #self.name=name                                               
        super().__init__(id,name)
        self.sal=sal
    def display(self):
        print(self.id,self.name,self.sal)

e=emp(1,"Ashutosh",230000)
e.display()
