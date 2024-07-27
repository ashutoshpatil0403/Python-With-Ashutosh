# USE OF IF-ELSE AND FINDING EVEN ODD USING CONtrol STATEMENTS

n=int(input("Enter the number :"))
if (n>0):
    print("Number is positive")
else :
    print("Number is Negative")    

if(n%2==0):
    print("This is Even number")
else:
    print("This is Odd number")        

#Problem 2

n=int(input("enter the number"))

if n%2==0 :
    print("Even number")
else :
    print("odd number")

#Problem 3
p=int(input("Enter the total number of working days :"))
q=int(input("Enter the total days of absent :"))

r=p-q
s=(r/p)*100
print("Your attendance percentage is :",s)
if s>=75:
    print("You are eligible to atend exam")
else : 
    print("You are not eligible to attend exam")    

        