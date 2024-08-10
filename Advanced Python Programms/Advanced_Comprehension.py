#Advanced Comprehension:

#26. Use the zip function with list comprehension to create a list of pairs from two lists.
list_1=[1,2,3,4]
list_2=['One', 'Two', 'Three', 'Four']
ziplist = [(i,j) for i,j in zip(list_1,list_2)]
print(ziplist)

#27.Create a generator expression to yield Fibonacci numbers up to 100.


#28.Implement a nested list comprehension to flatten a 2D list.
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattenlist = [number for row in matrix for number in row]
print(flattenlist)

#29.Write a dictionary comprehension using enumerate to map a list of words to their length and index.
words_list = ['Suresh', 'Vishnu', 'Vinay']
enumerate_dict = {word:(index, len(word)) for index,word in enumerate(words_list)}
print(enumerate_dict)

#30.Generate a list of tuples where each tuple contains two numbers from the range 1 to 5, but only if they are different.
list_tuple_diff = [(x,y) for x in range(1,5) for y in range(1,5) if x!= y]
print(list_tuple_diff)
