#Dictionary Comprehension:

#6 Build a dictionary where keys are numbers from 1 to 5, and values are their cubes.
cubes_dict = {i: i**3 for i in range(1, 6)}
print(cubes_dict)

#7 Create a dictionary with keys as vowels and values as their ASCII values.
ascii = {i: ord(i) for i in ['a', 'e', 'i', 'o', 'u']}
print(ascii)

#8 Write a dictionary comprehension to count the frequency of each character in a given string.
str = "welcome to india,hello how are you"
frequency= {i:str.count(i) for i in list(str)}
print(frequency)

#9 Generate a dictionary where keys are even numbers from 1 to 10, and values are their squares.
d={i:i**2 for i in range(1,11) if i%2==0}
print(d)

#10 Build a dictionary mapping words to their lengths in a given sentence.
a ="This is ashutosh patil and he is mechanical engineer"
word_len = {w: len(w) for w in a.split()}
print(word_len)
