# ====================================================== WHILE LOOP STATEMENT==============================================

n=1
while n<=10:
    n+=1
    if n%2==0:
        if n%4==0:
              print(n)

# Example 2=========================================
              
i=int(input("Enter the number :"))
sum=0
while i>0:
    sum=sum+i
    i=i-1
print("Sum of the n natural numbers :",sum)

# Example 2=========================================

i=1
while i<=10:
    print(i)
    i+=1    
              
# ================================================= FOR LOOP ============================================================= 

for s in range(1,51):
    print (s)

for e in range(0,101,2) :
    print(e)    

# Example 2 =========================================  

list=['1','2','3','4','5','6','7','8','9','10']
for k in list:
    print(k)

range(0,11,2)

# Example 3 =========================================

for i in range (1,6):
    for j in range (1,i+1):
        print("*",end =" ") 
    print("\n")  
            
# Example 4 =========================================             

sume=0
sumo=0
for q in range (0,50):
    if q%2==0:
        sume=sume+q
        print(sume)
    else:
        sumo=sumo+q
        print(sumo)

print(sume+sumo) 

# Example 5 =========================================             

sume=0
sumo=0
for q in range (0,50):
    if q%2==0:
        sume=sume+q
        print(sume)
    else:
        sumo=sumo+q
        print(sumo)

print(sume+sumo)      

# Example 6 =========================================             

for z in range (100,501):
    if z%11==0 and z%2!=0:
        print(z)

# Example 7 =========================================             
  
num=int(input("Enter the number:"))
for l in range(1,11):
    print(l*num)    

           
  