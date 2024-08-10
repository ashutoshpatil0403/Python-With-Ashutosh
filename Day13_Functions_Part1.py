def walking():
    print(" Get Up \n Brush Up \n Tie Shoe \n Take Water and Protien Booster")

walking()    

def avg(a,b,c):
    d=a+b+c
    e=d/3
    print("Average of given three numbers is :",e)

avg(68.62,87.60,76.1)    

#returns when only when we want by defining in any variable name
def purchase(item):
    return item

a=purchase("iphone")
print(a)

def add(a,b):
    c=a+b
    return c

d=add(23,45) # d is caller to call the return value
print(d)

# return saves multiple values
def mulval(a,b,c):
    add=a+b+c
    sub=a-b-c
    multi=a*b*c
    return add,sub,multi

all=mulval(10,22,43)
print(all)


def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        print(fact,end=" \n")
    
factorial(4)
    


