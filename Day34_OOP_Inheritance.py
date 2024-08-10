print("Today we will learn INHERITANCE")

# SINGLE INHERITANCE==========================================================================

class person:
    def hi(self):
        print("I am single inheritance")


class child(person):
    def show(self):
        print("Hey Hello in Karnataka") 

c=child()
c.show()
c.hi()               

# MULTIPLE INHERITANCE============================================================================

class parent1:
    def mybaby(self):
        print("HEllo World")

class parent2:
    def ind(self):
        print("Hello India")

class child(parent1,parent2):
    def kn(self):
        print("Hello Karnataka")

d=child()
d.mybaby()  
d.ind()
d.kn()

# MULTILEVEL INHERITANCE================================================================================

class Sc:
    def delhi(self):
        print("I am Supreme among all courts")

class hc(Sc):
    def mumbai(self):
        print("I am supreme in my state maharashtra")  

class dc(hc):
    def sangli(self):
        print("I am Supreme in my District i.e. Sangli ") 

j=dc()
j.delhi()
j.mumbai()
j.sangli()                     
    
# HEIRARCHIAL INHERITANCE=================================================================================
# bank is also a good example of this type. 
class laxman:
    def ld(self):
        print("100 acre jamin ahe mazi")

class BLP(laxman):
    def ppur(self):
        print("Mazi 33 ekre ahe tyatli")

class DLP(laxman):
    def d(self):
        print("MAzipn ahe")    

class SLP(laxman):
    def vrg(self):
        print("me too")

b=BLP()
d=DLP()
s=SLP()
b.ld()
b.ppur()
d.ld()
d.d()
s.ld()
s.vrg()
