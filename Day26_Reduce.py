from functools import reduce
lis=[1,2,3,4,5]
re=reduce(lambda a,b:a*b,lis)

print(re)

#WAPP TO PRINT FACTORIAL OF GIVEN NUMBER USING REDUCE FUNCTION

a=int(input("Enter the 1 number"))
b=int(input("Enter the 2 number"))
c=int(input("Enter the 3 number"))
d=int(input("Enter the 4 number"))


li=[a,b,c,d]
res=reduce(lambda p,q:p*q, li)
print(res)

