def sq(n):
    return n*n

lis=[1,2,3,4,5,6,7,8,9,10]

res=map(sq,lis)
print(list(res))   # NORMAL FUNCTION

l=lambda a: a*a

result=map(l,lis)
print(list(result)) # if we use set here then we get op but not in order

def up(msg):
    a=msg.upper()
    print(a)

l=["banglore","hyderabad"] 

res=map(up,l)
print(list(res))

l1=[1,3,5,7]
l2=[2,4,6,8]

ree=list(map(lambda a,b:a+b , l1 , l2))
print(ree)