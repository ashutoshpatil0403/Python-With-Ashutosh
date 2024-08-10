class customer:
    ifsc="SBI0302"
    def __init__(self,cname,cid,cno):
        self.cname=cname
        self.cid=cid
        self.cno=cno
    def update(self,cname,cid,cno):    
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

c.update("gau",2,876598765)
c.display()


# static method===============================================================================================
                                   # where ever common properties are there we use Static method
                                
class emp:
    def __init__(self,id) :
        self.id=id
    @staticmethod
    def staticmethod(a):
            print("I am static method")

e=emp(413)
print(e.id) 
e.staticmethod(1)
#emp.staticmethod(1)
#print(emp.id)         

# class methods======================================================================================

class inc:
     constituencyname="Raybareli"
     @classmethod
     def election(cls):
          print(cls.constituencyname)
          print("Loss INC Won BJP")
i=inc()
i.election()  #calling by object name
inc.election()   #calling by class name       

# how to update variable in classmethod

class inc:
     constituencyname="Raybareli"

     def __init__(self,mp) :
          self.mp=mp
     @classmethod
     def Resultelection(cls,newconstituency):
          cls.constituencyname=newconstituency
          print(cls.constituencyname)
          #print("Loss INC Won BJP")
i=inc("Shahu Maharaj")
i.Resultelection("Kolhapur")  
#inc.Resultelection() 

