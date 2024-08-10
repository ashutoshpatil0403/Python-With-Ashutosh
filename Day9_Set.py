# SET UNION
s={1,2,3,4,5,6,6,7,65634535}
print(s,type(s))
s1={3,4,0,98,32,43,}
print(s.union(s1))

s2={2,4,44,1}
s3={23,1}
s4={1,22,23}
print(s2|s3|s4)

print(s2.union(s,s1,s3,s4))

#INTERSECTION 
s={1,2,3,4,5,6,6,7,65634535}
print(s,type(s))
s1={3,4,0,98,32,43,}
print(s.intersection(s1))

s2={2,4,44,1}
s3={23,1}
s4={1,22,23}
print(s2&s3&s4)

print(s2.intersection(s,s1,s3,s4))

#Diference
s5={1,2,3,4}
s6={2,4,5,6,7}
print(s5.difference(s6))
print(s6.difference(s5))

#opposite to intersection SYMMETRIC_DIFFERENCE

s5={1,2,3,4}
s6={2,4,5,6,7}
print(s5.symmetric_difference(s6))
print(s6.symmetric_difference(s5))

#CONVERSION 
b=list(s5)
print(b)
print(type(b))
b=tuple(s5)
print(b)
print(type(b))
b=set(s5)
print(b)
print(type(b))

#ADD METHOD
m={1,2,3,4}
m.add(5)
print(m)

a={'a','e','i'}
b=('o','u')
a.add(b)
print(a)

ss={10,20,30,40,50}
print(ss)
print(ss.remove(30))
print(ss.discard(100))
print(ss.pop())

n={12,23,34}
nm={23,43,21}
n.difference_update(nm)
print(n)
nm.difference_update(n)
print(nm)

#DISJOINT
p={1,22,3}
q={2,33,3}
print(p.isdisjoint(q))
p1={1,22,3}
q1={2,33,4 }
print(p1.isdisjoint(q1))

#SUBSET
p2={2,3}
q2={2,3,4,5}
r2={17.9,9,1}
print(p2.issubset(q2))
print(r2.issubset(q2))

#SUPERSET: ViceVersa of SUBSET 

#update

s1={1,2,3}
s2=[2,44,55,66]
s1.update(s2)
print(s1)

set1={1,2,34,5,6,74,45,10,7,8,7,87,6,5,77,5,22,24}
set2={11,22,33,44,5,55,6,66,7,2,888,9,00,12,24}
list=[1,2,3,44,54,23,54]
print(set1.update(list))
print(set1.difference(set2))
print(set1)
print(set1.difference(set2))
q4=set2.difference(set1)
print(set1.update(q4))
print(q4)
set1.remove(34)
print(set1)
print(set1.symmetric_difference(set2))
print(set1.intersection(set2))
print(set1.union(set2))
print(set1.update(set2))
print(set1.intersection_update(set2))