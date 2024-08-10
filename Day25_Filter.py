def even(n):
    if n%2==0:
        print(n)

lis=[1,2,3,4,5,6,7,78,8,89,9656,452,55,1,5,5,543535,553,5,5,66,3,535,636]

result=list(filter(even,lis))
print(result)

r=list(filter(lambda a:a%2==1 , lis))
print(r)