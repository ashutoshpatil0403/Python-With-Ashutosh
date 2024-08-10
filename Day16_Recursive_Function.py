def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
factorial=fact(4)
print(factorial)
#====================================================================================================================
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
for i in range(5):
    print(fibonacci(i))
#====================================================================================================================
def reverse(n):
    if n<=1:
        return n
    else:
         for i in range (0,n+1):
             print(i)
reverse(5)            
#================================================================================================================
def print_numbers(n):
    if n == 0:
        return
    print(n)
    print_numbers(n - 1)

print_numbers(5)
 