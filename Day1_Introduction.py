#Declaration of Variable in python. Variable is like container which stores values 
a=10
#To retrieve stored values in variable we are using print in built method
print(a)

# this is comment in python
# Comments are such pat of the code which can not interpreted or compiled by interpreter or compiler

#Types of variable: to find type of stored value we can use type in built method
#integer,string,booloean,float,none,complex
print(type(a))

i=4     #integer
s='ashutosh'    #string
b=True  #boolean
f=4.67  #float
n=None #nonetype
c=5+2j #complex
print(type(i),type(s),type(b),type(f),type(n),type(c))

#How to take input from user in python 
#.. We can use input method to take input from user
#.. By default input datatype is string . if want to use that input as int datatype then we have to typecast it   
number1=input("Enter number1 :")
number2=input("Enter number2 :")
#@sum=number1+number2   #here we not typecasted num1 and num2 so our output is like 34 + 12 = 3412
num1=int(number1)    # here we typecasted from string to integer
num2=int(number2)     # here we typecasted from string to integer      
sum=num1+num2
print(sum)   # 34 + 12 = 46

# input method
a=input("enter the first number =")
a=int(a)
print(a)
b=int(input("enter second number ="))
print(b)
c=a+b
print("Addition is =",c)

# type casting {TYPE CONVERSION}

a=10
b=float(a)
print(a,type(a))
print(b,type(b))
c=complex(a)
print("hello world")

