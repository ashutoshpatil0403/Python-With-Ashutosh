name = "ashutosh patil in completed mechanical engoineering in may 2021 "
print(len(name))
# Slicing In String============================= 
print(name[0:9])
len=len(name)
print("Length of name string is ",len)
print(name[0:-50])
nm="harry"
print(nm[-4:-2])

#reversed string
txt = "Hello World"[::-1]
print(txt)


#remove vowels from given string
s=input("Enter the String")
print(s)
vowel=['a','e','i','o','u','A','E','I','O','U']

newtext=""
for i in s:
    if i not in vowel:
        newtext=newtext+i
print(newtext,end=" ") 

"""Write a program that creates a list of 10 random integers. Then create two lists by

name odd_list and even_list that have all odd and even values of the list respectively"""

list=[1,2,3,4,5,6,6,7,8,8,9,10]
evenlist=[]
oddlist=[]
for j in list:
    if j%2==0:
        evenlist.append(j)
print(evenlist)
for k in list:
    if k%2==1:
        oddlist.append(k)
print(oddlist)
