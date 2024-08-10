print("Match case by Code With Harry")

x=int(input("Enter the value of x :"))

match x:
    case 0:
        print("x is zero")
    case 3:
        print("x is three")
    case _ if x!=90:
        print("x is not equal to 90")        
    case _ :
        print("Super class battery check")    