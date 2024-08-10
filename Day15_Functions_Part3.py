print("FUNCTION VATIABLE")
a=1
def access():
    a=a+1
    print(a)
print(a)

def addition(*a):
    sum=0
    for i in a:
        sum=sum+i
    print(sum)

addition(2,4,8,55,77,33)
cc=3
def add(a,b):
    c=2
    d=(a+b)/c
    print(a)
    print(b)
    print(d)
add(354,879)

print(cc)
def add(a,b,c):
    d=(a+b+c)/cc
    print(a)
    print(b)
    print(c)
    print(d)
add(354,879,345)

# UPDATE GOBAL V INSIDE LOCAL VARIABLE
aa=10
def access():
    global aa
    aa=aa+10
    print(aa)
access()