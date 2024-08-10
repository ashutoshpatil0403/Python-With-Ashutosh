def access():
    yield 1

print(access())    # generator object is generated method 1
print(next(access()))

res =(i for i in range(1,10))
print(res)         # generator object is generated method 2
for a in res:
    print(a , end=" ")



def add(a,b):
    c=a+b
    yield c
a=add(3,4)
print(next(a))    #or
for i in add(75,87):
    print(i)

    #========================================================

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_gen = fibonacci()
#print(next(fib_gen))
for i in range(10):
    print(next(fib_gen), end=" ")        
    
#generate fibonacci series using generator function
def fibonacci(num):
    a,b=0,1
    while a<0:
        yield a
        a,b=b,a+b
x= fibonacci()
for i in range(10):
    print(next(x),end=" ")
#x=fibonacci(8)
#print(next(x))

    