def outer(fun):
    def inner(a):
        b=fun(a)
        return b.upper()
    return inner

@outer
def display(msg):
    return msg
print(display("Welcome"))

#========================================Decoration with two parameters=======================================================================

def avg(fun):
    def inner(p,q):  
        e=fun(p,q)
        return e/2
    return inner

@avg
def addition(a,b):
    return a+b
print(addition(5,88))