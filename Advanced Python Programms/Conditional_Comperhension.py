#Conditional Comprehension:
#21. Write a list comprehension to get only even squares from the numbers 1 to 10.
list_even_squares = [x**2 for x in range(1,10) if x**2 %2 == 0]
print(list_even_squares)

#22.Create a dictionary comprehension to exclude items with values less than 5 from a given dictionary.
dictionary = {2: 4, 4: 16, 6: 36, 8: 64}
value_less_5 = {key: value for key,value in dictionary.items() if value > 5}
print(value_less_5)

#23.Generate a list of numbers from 1 to 50 that are divisible by either 3 or 5 using conditional list comprehension.
divisible_by_3_or_5 = [x for x in range(1,50) if (x%3 == 0 or x%5==0)]
print(divisible_by_3_or_5)

#24.Build a list of strings from a given list, excluding those with a length less than 4.
sentence = "Build a list of strings from a given list, excluding those with a length less than 4"
sentence_list = sentence.split(" ")
list_of_str_4 = [x for x in sentence_list if len(x) > 4]
print(list_of_str_4)

#25.Write a set comprehension to get the squares of even numbers and cubes of odd numbers from 1 to 10.
square_and_cubes = {x **2 if x%2== 0 else x**3 for x in range(1,10)}
print(square_and_cubes)




