def outer(function):
    def inner():
        a=function()
        return a.upper()
    return inner

@outer
def access():
    return "welcome"
print(access())

#  DECORATORS ======================================

def new(function):
    def old():
        s=function()
        return s.split()
    return old

@new
def string():
    return "hello world this is india"
print(string())

# CHAINING OF DECORATORS=======================================================================       

def chain(func):
    def c():
        a=func()
        return a.upper()
    return c

def chainn(funn):
    def cc():
        b=funn()
        return b.split()
    return cc

@chainn
@chain
def chaining():
    return "india is my country and i love my india"
print(chaining())

#===================================================================================================================

def chain(func):
    def c():
        a=func()
        return a*a*a
    return c

def chainn(funn):
    def cc():
        a=funn()
        return a/2
    return cc

@chainn
@chain
def chaining():
    return 10
print(chaining())
























