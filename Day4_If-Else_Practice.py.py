
#Problem 1===================================================================================

age=int(input("Enter your age :"))
if age>=18 :
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")    

#Problem 2===================================================================================

n=int(input("Enter the number :"))
if(n%2==0):
    print("This is Even number")
else:
    print("This is Odd number")

#Problem 3===================================================================================

m=int(input("Enter the number :"))
if(m%7==0):
    print("Given number is divisibe by 7")
else:
    print("Given number is not divisible by 7")

#Problem 4===================================================================================

o=int(input("Enter the number :"))
if(o%5==0):
    print("Hello")
else:
    print("Bye")

#Problem 5===================================================================================

unit=int(input("Enter your consumed UNITS :"))
if unit<=100:
    print("Your Electricity Bill Is :",unit,"Rs")    
elif unit>100 and unit<=200:
    print("Your Electricity Bill Is :",unit*5,"Rs")
else:
    print("Your Electricity Bill Is :",unit*10,"Rs")

#Problem 6===================================================================================

p=int(input("Enter the number :"))
print("Last digit of entered number is :",p%10)

q=int(input("Enter the number :"))
r=q%10
if r%3==0:
    print("Last digit of given number is divisible by 3")
else:
    print("Last digit of given number is not divisible by 3")   

#Problem 7===================================================================================

perc=int(input("Enter your percentage :"))
if perc>90:
    print("Grade=A")
elif perc>80 and perc<=90:
    print("Grade=B")
elif perc>60 and perc<=80:
    print("Grade=C")
else:
    print("Grade=D")

#Problem 8===================================================================================

cp=float(input("Enter the cost price of the bike :"))
if cp>100000:
    print("Total Tax is ",cp*0.15)
elif cp>50000 and cp<=100000:
    print("Total Tax is ",cp*0.1)    
else :
    print("Total Tax is ",cp*0.05)

#Problem 9===================================================================================

year=int(input("ENter the year :"))
if year%4==0 :
    print("Entered year is leap year")
elif year%400==0:
    print("Entered year is leap year")
else:
    print("Entered year is not a leap year")    

#Problem 10===================================================================================

day=int(input("Enter the number from 1 to 7"))
if day==1:
    print("Sunday")
elif day==2:
    print("Monday") 
elif day==3:
    print("Tuesday")
elif day==4:
    print("Wednesday")
elif day==5:
    print("Thursday")
elif day==6:
    print("Friday")
elif day==7:
    print("Saturday")
else:
    print("Please enter number from 1 to 7")

#Problem 11===================================================================================

y=int(input("enter the number of which you want month and total days in that month"))

if y==1:
    print("Month is January and total days are 31")
elif y==2:
    print("Month is Febrary and total days are 29/28 depending on Leap year")
elif y==3:
    print("Month is March and total days are 31")
elif y==4:
    print("Month is April and total days are 30")
elif y==5:
    print("Month is May and total days are 31")
elif y==6:
    print("Month is june and total days are 30")
elif y==7:
    print("Month is July and total days are 30")
elif y==8:
    print("Month is August and total days are 31")
elif y==9:
    print("Month is Septamber and total days are 30")
elif y==10:
    print("Month is october and total days are 31")
elif y==11:
    print("Month is November and total days are 30")
elif y==12:
    print("Month is December and total days are 31")
else :
    print("Month Does not exist")

#Problem 12===================================================================================

pp=input("Enter your percentage :")
pp=int(pp) 
print(pp)

if pp>=80 and pp==100:
    print("A+")
elif pp<80 and pp>=60:
    print("A")
elif pp<60 and pp>=50:
    print("B+")
elif pp<50 and pp>=45:
    print("B")
elif pp<45 and pp>=25:
    print("C")
elif pp<25:
    print("D")         
else:
    print("Wrong Percentage")    

#Problem 13===================================================================================

service=int(input("Enter your service experience :"))
sal=int(input("Enter your salary :"))
if service>10:
    print("salary with bonus is :",(sal*0.10)+sal)
elif  service<=10 and service>=6:
    print("salary with bonus is :",(sal*0.08)+sal)
else: 
    print("salary with bonus is :",(sal*0.05)+sal)        

#Problem 14===================================================================================
                                                           
p=input("Enter your percentage :")
p=int(p) 
print(p)

if p>=95 and p==100:
    print("Congratulations you are in EXTINCTION")
elif p<95 and p>=85:
    print("Very Good Performance")
elif p<85 and p>=70:
    print("Good Performance")
elif p<70 and p>=60:
    print("Poor performance")
elif p<60 and p>=50:
    print("Very Poor Performance")
elif p<50 and p>=35:
    print("Bad Performance")
elif p<35 and p>=0:
    print ("FAILED")                       
else :
    print("Entered wrong percentage")    

#Problem 15===================================================================================

magnitude=input("Enter the scale of earthquake")
magnitude=float(magnitude)

if magnitude>1.0 and magnitude<2.0:
         print("Microearthquakes not felt or rarely felt") 
elif magnitude>2.0 and magnitude<4.0: 
         print("Very rarely causes damage")
elif magnitude>4.0 and magnitude<5.0:
         print("Damage done to weak buildings") 
elif  magnitude>5.0 and magnitude<6.0:
         print("Cause damage to the poorly constructed building")
elif  magnitude>6.0 and magnitude<7.0:
         print("Causes damage to well-built structures")
elif  magnitude>7.0 and magnitude<8.0:
         print("Causes damage to most buildings")
elif  magnitude>8.0 and magnitude<9.0:
         print("Causes major destruction")
elif  magnitude>9.0 :
        print("Causes unbelievable damage")
else :
  print("welcome to Heaven")