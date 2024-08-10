#Nested List
# 16.Create a list of lists where each inner list contains the first three multiples of the corresponding number in the outer list.
l1 = [1, 2, 3, 4, 5]
list = [[n*1, n*2, n*3] for n in l1]
print(l1)

#17.Generate a nested dictionary where keys are numbers from 1 to 3, and values are dictionaries with keys as numbers from 1 to 5 and values as their squares.
nested_dict = {outer: {inner: inner**2 for inner in range(1, 6)} for outer in range(1, 4)}
print(nested_dict)
print(nested_dict.values())

#18.Build a list of tuples where each tuple contains a letter and its corresponding ASCII value for all letters in the word "PYTHON".
word = "PYTHON"
tuples = [(l, ord(l)) for l in word]
print(tuples)

w='ASHUTOSH'
v=[(z,ord(z)) for z in w]
print(v)

#19.Create a list of lists where each inner list contains numbers from 1 to the outer list's index.(Take Help From ChatGPT)
outer_list = 5  
nested_lists = [[i for i in range(1, index + 1)] for index in range(1, outer_list + 1)]
print(nested_lists)

#20.Generate a nested set where each inner set contains vowels from a word and its reverse. (Not Understanding)
#word="ashutoshpatil"
#w=set(word)
#set_={{i for i in word for i in ['a','e','i','o','u'],w[::-1]}  }