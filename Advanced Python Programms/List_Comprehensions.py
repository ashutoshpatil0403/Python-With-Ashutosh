#List Comprehension

import math
#1 Generate a list of even numbers from 1 to 20 using list comprehension.
even_numbers = [x for x in range(1, 21) if x % 2 == 0]
print(even_numbers)

#2 Create a list of cubes for the numbers 1 to 10 using list comprehension.
cube=[i**3 for i in range(1,11)]
print(cube)

#3 Write a list comprehension to get the square roots of numbers from 1 to 10.
sqrt=[math.sqrt(i) for i in range(1,11)]
print(sqrt)

#4 Generate a list of strings by concatenating each number from 1 to 5 with the letter 'A'
string = [str(x) + 'A' for x in range(1, 6)]
print(string)

#5 Create a list of tuples where each tuple contains a number and its square.
result=[(i,i*i) for i in range(1,11)]
print(result) 
