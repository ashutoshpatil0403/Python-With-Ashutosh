def add(a,b):
    c=a+b
    return c

add(3,4)

#LAMBDA FUNCTOIN=====================================================================================

res = lambda a,b : a+b
print(res(4,3))
print(res(23,45))

s="welcome"
print(s.upper())


string=lambda a: a.upper()
print(string("welcome"))

def access (*n):
    sum=0
    for i in n:
        sum=sum+i
    print(sum)

access(1,2,3,4,5,6,7,8,9,10)        

result=[i for i in range(0,11) ] 
print(result)

rr=lambda : [x   for x in range(1,11)]
print(rr)

#rrr=[lambda x:x((x) for i in range(0,11))]
#print(rrr)

sq= lambda : [x**2 for x in range(1,11) ]
print(sq())
rr=lambda : [x*x   for x in range(1,11)]
print(rr())

ss=[(lambda x:x)(x*x) for x in range(1,11)]
print(ss)

ip=input("Enter the string")
s1= lambda str:str.upper()
print(s1(ip))

s2= lambda str:str.title()
print(s2(ip))

s3= lambda str:str.replace("a","A")
print(s3(ip))

dil=[(lambda ip:ip.upper())(i) for i in ip]
print(dil) 