# Prime Number Checking

num=int(input("Enter the number:"))
for l in range(2,num):
    if num%l==0:
        print("Not a prime number")
        break
else:
    print("Prime number")        

# Perfect Number Checking

sum=0    
number=int(input("Enter the number"))

for i in range(1,number):
    if number%2==0:
        sum=sum+i
    if sum==number:
        print("number is perfect")
    else:
        print("Number is not perfect")  
        break       
    
# ARMSTRONG NUMBER 
arm=int(input("Enter the number :"))
summ=0
tempp=arm
while arm>0:
    rem=arm%10
    summ=summ+(rem**3)
    arm=arm//10
print(summ)
if summ==tempp:
    print("No is armstrong")
else :
    print("No is not armstrong")        


#Palaondrom=================================================================================
pal=int(input("Enter the number :"))
rev=0
temp=pal

while pal>0:
    rem=pal%10
    rev=rev*10+rem
    pal=pal//10
print(rev)    
if rev!=temp:
    print("Number is not palumdrum ")
else:
    print("Number is panundrum")    



# REVERSE NUMBER ===================================================================================================
num=int(input("Enter the number :"))
rev=0

while num>0:
    rem=num%10
    rev=(rev*10)+rem
    num=num//10
print("Reverse of given number :",rev)    


# sum of n natural numbers============================================================================================
n=int(input("Entert the number :"))
sum=0
i=0

while( i<=n):
    sum=sum+i
    i=i+1
print ("Sum =",sum)

# ==================================COMMENT IS HERE====================================

name=input("What is yoour name")
print("Hello" + name)
    
# Factorial Number Programm

n =int(input("Enter the number"))
fact = 1
 
for i in range(1, n+1):
    fact = fact * i
 
print("The factorial of",n ,"is :", fact)
print(fact)    

# Fibonacci Series Programmm

n=int(input("Enter the number :"))
n1=0
n2=1
sum=0

if n<0:
    print("Enter positive number")
else:
    for i in range (0,n):
        print(sum)#print(sum,end=" ")
        sum=n1+n2 
        n1=n2
        n2=sum
          
