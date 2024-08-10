# Exercise 1: Convert two lists into a dictionary
def convert_lists_to_dict(list1, list2):
    return dict(zip(list1, list2))

list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
result1 = convert_lists_to_dict(list1, list2)
print("Exercise 1:", result1)

# Exercise 2: Merge two Python dictionaries into one
def merge_dicts(dict1, dict2):
    result = dict1.copy()
    result.update(dict2)
    return result

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
result2 = merge_dicts(dict1, dict2)
print("Exercise 2:", result2)

# Exercise 3: Print the value of key ‘history’ from the below dict
sample_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}

def get_history_value(sample_dict):
    return sample_dict["class"]["student"]["marks"]["history"]

result3 = get_history_value(sample_dict)
print("Exercise 3:", result3)

# Exercise 4: Initialize dictionary with default values
def initialize_dict_with_defaults(keys, default_value):
    return dict.fromkeys(keys, default_value)

keys = ['key1', 'key2']
default_value = 0
result4 = initialize_dict_with_defaults(keys, default_value)
print("Exercise 4:", result4)

# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
def extract_keys_to_dict(original_dict, keys):
    return {key: original_dict[key] for key in keys if key in original_dict}

original_dict = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
keys_to_extract = ['name', 'salary']
result5 = extract_keys_to_dict(original_dict, keys_to_extract)
print("Exercise 5:", result5)

# Exercise 6: Delete a list of keys from a dictionary
def delete_keys_from_dict(original_dict, keys):
    for key in keys:
        if key in original_dict:
            del original_dict[key]
    return original_dict

original_dict = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
keys_to_delete = ['name', 'salary']
result6 = delete_keys_from_dict(original_dict, keys_to_delete)
print("Exercise 6:", result6)

# Exercise 7: Check if a value exists in a dictionary
def check_value_exists(dictionary, value):
    return value in dictionary.values()

sample_dict = {'a': 100, 'b': 200, 'c': 300}
value_to_check = 200
result7 = check_value_exists(sample_dict, value_to_check)
print("Exercise 7:", result7)

# Exercise 8: Rename key of a dictionary
def rename_key_in_dict(dictionary, old_key, new_key):
    dictionary[new_key] = dictionary.pop(old_key)
    return dictionary

sample_dict = {'name': 'Kelly', 'age': 25, 'salary': 8000, 'city': 'New York'}
old_key = 'city'
new_key = 'location'
result8 = rename_key_in_dict(sample_dict, old_key, new_key)
print("Exercise 8:", result8)

# Exercise 9: Get the key of a minimum value from the following dictionary
def get_min_value_key(dictionary):
    return min(dictionary, key=dictionary.get)

sample_dict = {'Physics': 88, 'Math': 75, 'Chemistry': 72, 'Biology': 89}
result9 = get_min_value_key(sample_dict)
print("Exercise 9:", result9)

# Exercise 10: Change value of a key in a nested dictionary
def change_nested_dict_value(dictionary, key, subkey, new_value):
    dictionary[key][subkey] = new_value
    return dictionary

sample_dict = {
    'emp1': {'name': 'John', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}
key = 'emp3'
subkey = 'salary'
new_value = 8500
result10 = change_nested_dict_value(sample_dict, key, subkey, new_value)
print("Exercise 10:", result10)
