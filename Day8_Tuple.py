# Tupples are immmutable
t1=(1,2,3,4,5)  #or t1=1,2,3,4,5,7
print(t1)
print(type(t1))

t2= tuple(range(1,20))
print(t2)
print(type(t2))

#Length
print(len(t1))

#Concatenation
print(t1+t2)

#Repetition
print(t1*3)

#Iteration
for i in  t1:
    if i%2==0:
        print("Even NUmber :",i)

#menbership
print(2 in t1)        

t3=(1,23,45,'ashu',22,87.60)
print(t3)
t4=[1,2,3,4,"ashu",234,87]
print(t4)
print(t4[1:4:2])
print(t4[3])
print(t4.index(4))