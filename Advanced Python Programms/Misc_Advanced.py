
#31. Write a list comprehension to filter out duplicate elements from a list.
#Solution:
def filter_duplicates(lst):
    return [x for i, x in enumerate(lst) if x not in lst[:i]]

#32. Generate a list of random numbers using list comprehension and the random module.
#Solution:
import random
def generate_random_numbers(n, start=0, end=100):
    return [random.randint(start, end) for _ in range(n)]

#33. Create a dictionary from two lists, one for keys and another for values, using dictionary comprehension.
#Solution:
def create_dict(keys, values):
    return {k: v for k, v in zip(keys, values)}

#34. Build a set of lowercase characters from a given string using set comprehension.
#Solution:
def lowercase_set(string):
    return {char.lower() for char in string if char.isalpha()}

#35. Write a list comprehension to find common elements in two lists.
#Solution:
def common_elements(lst1, lst2):
    return [x for x in lst1 if x in lst2]

#36. Generate a list of the lengths of words in a given sentence using list comprehension.
#Solution:
def word_lengths(sentence):
    return [len(word) for word in sentence.split()]

#37. Create a list of squares for even numbers and cubes for odd numbers from 1 to 10 using a lambda function and list comprehension.
#Solution:
def squares_and_cubes():
    return [(lambda x: x**2 if x % 2 == 0 else x**3)(x) for x in range(1, 11)]

#38. Write a set comprehension to get unique words from a sentence, ignoring case.
#Solution:
def unique_words(sentence):
    return {word.lower() for word in sentence.split()}

#39. Generate a list of numbers from 1 to 20, replacing prime numbers with 'Prime' using a function and list comprehension.
#Solution:
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_replace():
    return ['Prime' if is_prime(x) else x for x in range(1, 21)]

##40. Create a dictionary where keys are words from a sentence, and values are their lengths using a function and dictionary comprehension.
#Solution:
def word_length_dict(sentence):
    return {word: len(word) for word in sentence.split()}

#41. Read a file containing numbers and create a list of integers using list comprehension.
#Solution:
def list_of_integers_from_file(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

#42. Generate a dictionary where keys are words from a text file, and values are the number of occurrences using dictionary comprehension.
#Solution:
def word_count_dict(file_path):
    with open(file_path, 'r') as file:
        text = file.read().split()
        return {word: text.count(word) for word in set(text)}

#43. Create a set of unique words from a text file using set comprehension.
#Solution:
def unique_words_set(file_path):
    with open(file_path, 'r') as file:
        return {word for word in file.read().split()}

#44. Write a list comprehension to filter out lines containing a specific word from a text file.
#Solution:
def filter_lines(file_path, word):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file if word not in line]

#45. Generate a list of tuples, each containing a line number and the corresponding line from a text file using list comprehension.
#Solution:
def line_number_tuples(file_path):
    with open(file_path, 'r') as file:
        return [(i + 1, line.strip()) for i, line in enumerate(file)]

#46. Read a list of integers from user input, handling exceptions using list comprehension.
#Solution:
def list_of_integers_from_input(input_str):
    return [int(x) for x in input_str.split() if x.isdigit()]

#47. Create a dictionary from user input, allowing the user to continue entering key-value pairs until they decide to stop, using dictionary comprehension.
#Solution:
def input_to_dict(input_str):
    return {k: v for k, v in (pair.split(':') for pair in input_str.split(','))}

#48. Write a list comprehension to filter out non-numeric elements from a list entered by the user.
#Solution:
def filter_non_numeric(input_list):
    return [x for x in input_list if isinstance(x, (int, float))]

#49. Generate a set of valid email addresses from a list of strings using set comprehension and a regular expression for email validation.
#Solution:
import re
def valid_emails(input_list):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return {email for email in input_list if re.match(email_regex, email)}

#50. Create a list of integers from user input, handling invalid inputs using list comprehension and try-except blocks.
#Solution:
def safe_integers(input_str):
    return [int(x) for x in input_str.split() if x.isdigit()]
