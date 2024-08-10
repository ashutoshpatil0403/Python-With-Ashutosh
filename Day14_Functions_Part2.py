# WAPP TO FIND SI USING FUNCTUION

#POSITIONAL ARGUMENTS:
def simpleinterest(p,t,r):
    si=(p*t*r)/100
    print("Simple Interest=",si)

simpleinterest(100000,5,8.04)    

#KEYWORD ARGUMENTS
def simpleinterest(p,t,r):
    si=(p*t*r)/100
    print("Simple Interest=",si)

simpleinterest(100000,3,r=6.5)  
#DEFAULT ARGUMENTS
def Sinfo(name,age,dob,grade,doj="2023-12-18"):
    print(name,age,dob,grade,doj)

Sinfo("ashutosh",23,"2000-03-04","A+")   

#VARIABLE LENGTH ARGUMENT
def add(*a):
    for i in a:
        print(i)
add(1,2,3,4,5,6,7,9,10)    

def addition(*a):
    sum=0
    for i in a:
       sum=sum+i
    print(sum)
    
addition(81,52,783,94)

#VARIABLE KEYWORD LENGTH ARGUMENTS
def display(**ar):
    for key,value in ar.items():
        print(key,value)

display(a=10,b=20,c=30)        
#================================================different combinations====================================================

def combi(*a,**aa):
    for i in a:
        print(i)
    for j,k in aa.items(): 
        print(j,k)

combi(1,2,3,4,mark=70,name="Ashutosh",CGPA=9.02)           


     
