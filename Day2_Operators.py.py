#Operators in Python 
#...Arithmetic Operators
a=10
b=11
c=45
print("a+b =",a+b)
print("a-b =",a-b)
print("a*b =",a*b)
print("a/b =",a/b)
print("a**b =",a**b)
print("a//b =",a//b)
print("a%b =",a%b)


#...assignment operator(different way of writing arithmetic operators)
p=2
q=3

p+=q
print(p)

p/=q
print(p)

p*=q
print(p)

p%=q
print(p)

p-=q
print(p)


#... Comparisional Operators or Relational Opertors
print("a>b =",a>b)
print("a<b =",a<b)
print("a>=b =",a>=b)
print("a<=b =",a<=b)
print("a!=b =",a!=b)
 

#...Bitwise Operators

x=5
y=6
z=6
print (x<y and x==y)
print (x>y and x!=y)
print (not (x==y and x<y))
# bitwise operator conversion from decimal to binary go there and use and , or operator do operation and result is in binary form so again convert into decimal by using bit method shortcut i.e. 7bit: 4 2 1 rule and 16bit: 8 4 2 1
# see notebook for more understanding
print(x&y)
print(x|y)
# membership operator
print('a' in "banglore")
print('b' not in "Manglore")
# identity operator IS , IS NOT
print(a is b)
print(a is not b)

print(hash(a))
print(hash(b))
print(a is b)

# today is 2024-02-21
