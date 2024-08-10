#nested functoin
def oouter():
    def r():
        print(" Hello Ashutosh")
    r()
oouter()       


def outer(fname,lname):
    def inner():
        print(fname+lname)
    inner()
outer("banglore","Karnataka")


def add(a):
    def add2(b):
        print(a+b)
    add2(4)
add(5)   

def out():
    msg="hi"
    def inn():
        
        msg="bye"
        print(msg)
    inn()
out()       
   # nested function and inner function is both are same
def out():
    msg="hi"
    print(msg)
    def inn():
        global msg
        msg="bye"
        print(msg)
    inn()
    print(msg)
out() 

#Closure in python

def outer():
    X=3
    def inner():
        Y=3
        return X*Y
    return inner()
a=outer()
print(a)

