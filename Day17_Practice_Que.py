# WAP TO COUNT THE OCCURANCE OF EACH WORD IN A SENTENCE
# WAP TO CHECK IF A STRING IS A VALID EMAIL ADDRESS OR NOT
# FIND THE COMMON ELEMENTS BETWEEN TWO TUPLES  "done"
# COUNT THE NO OF EVEN AND ODD NUMBERS IN A TUPLE
# WAP TO FIND NON REPEATED CHARACTER IN A STRING

# FIND THE COMMON ELEMENTS BETWEEN TWO TUPLES  
a=(1,2,3,4,5)
b=(22,33,44,5,44,1)
aa=set(a)
bb=set(b)
c=aa.intersection(bb)
print(c)
d=tuple(c)
print(type(d))
print(d)

# COUNT THE NO OF EVEN AND ODD NUMBERS IN A TUPLE
tt=(1,2,3,4,5,56,7,8,96,54,35,32,3,4,5,65,7,87,56,544,3,23,3221,5,43,5,65433,434,45,4)
print(tt)
even=[]
odd=[]
for i in tt:
    if i%2==0:
        even.append(i)
    else :
        odd.append(i)
print(even)
print(odd)
oo=len(odd)
ee=len(even)
print("Total number of even numbers in tuple are",ee)
print("Total number of odd numbers in tuple are",oo)
