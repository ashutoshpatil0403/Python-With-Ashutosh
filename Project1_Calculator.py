# Python Calculator By Using Control Statements

a=input("enter the first number:")
b=input("enter the second number:")
a=int(a)
b=int(b)
operator =input("choose any operator +,-,*,/,%")

if operator =="+":
    print("Addition is :",a+b)
elif  operator =="-":
    print("Substration is :",a-b)
elif  operator =="*":
    print("Multiplication is :",a*b)
elif  operator =="/":
    print("Division is :",a/b)
elif  operator =="%":
    print("Remainder after a/b is :",a%b) 
else : print("Wrong operator entered")   