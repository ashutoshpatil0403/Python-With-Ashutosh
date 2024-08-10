import pandas
print("hi")
import hashlib
import math

print(math.factorial(5))
print(math.sqrt(12008))
print(math.sqrt(25))

print(math.ceil(5.8))

print(math.floor(5.2))

print(math.pow(5,3))

print(math.gcd(6,2))

#================================Module::: Random=======================================================
import random

for i in range(10):
    print(random.random())


print('--------')

for j in range(1,10):
    print(random.randint(1,10))

print('----------')

for k in range(10):
    print(random.uniform(20,50))

print('----------')

for k in range(10):
    print(random.randrange(10,20,2))


list1=['java','python','php','.net','cpp']

for i in range(5):
    print(random.choice(list1))

 