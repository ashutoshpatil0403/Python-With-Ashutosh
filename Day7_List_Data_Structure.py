#=================================================== List Datatype===========================================================

# APPEND ==============================================
list = [10,20,30]
list.append(40)
print(list)

list.append(50)
print(list)

#EXTEND  ===================================================
A=[10,20]
B=[30,40]
print(A+B)

A.extend(B)
print(A)

B.extend(A)
print(B)

# COPY METHOD  ===================================================
p1=[10,20,30]
p2=p1.copy()
print(p1)
print(p2)
print(p1 is p2)

# SORT METHOD   ===================================================
a=[10,2,4,11,3]
print(a)
a.sort()
print(a)

# REVERSE METHOD ===================================================
b=[2,3,4,5,6,0]
b.reverse()
print(b)
print(b[::-1])
for i in enumerate (b):
    print(b)

# SORT METHOD DESENDING ===================================================
    c=[10,20,5,200,40,34,300,297,302]
    print(c)
    c.sort()
    print(c)
    c.sort(reverse=True)
    print(c)    
    
# INSERT METHOD =================================================== 
    d=[0,12,13,14,16,17]
    d.insert(4,15)
    print(d)
    
# COUNT METHOD  ===================================================
    e=[10,20,30]
    print(e)
    print(e.count(30))

# REMOVE AND POP METHOD  ===================================================
    f=[12,2,3,3,4,3,43,32,2,23]  
    f.remove(32)
    print(f)  
    f.pop(2)
    print(f)
    f.pop()
    print(f)

    # INDEX METHOD  ===================================================
    g=[10,20,30,40]
    print(g.index(30))
    print(g.index(10,0,3)) # checks the position of 10 is present or not between 0,1,2 in this index position 

    # INDEXING ===================================================
    h=[10,20,30,40,50]
    print(h)
    h[0]=100
    h[1]=200
    h[2]=300
    h[3]=400
    h[4]=500
    print(h)
    
    # MULTIPLE VALUES UPDATION  ===================================================
    h[0:2]=250,200
    print(h)

    #WAPP TO PRINT 10,20,30,50,100 ===================================================
i=[10,20,30,50,100,20,10]
print(i.remove(20))
print(i.pop())
print(i.sort())
print(i)

res = []
for j in i:
    if j not in res:
        res.append(j)

print(res)

# delete  ===================================================
k=[10,20,30]
del k[2]
print(k)
k[1 ]=33
print(k)