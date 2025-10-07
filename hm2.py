# List Squarer: Write square_all(nums) that returns a new list containing the squares of all numbers.

def square_all(nums):
    return [i**2 for i in nums]
print(square_all([1,2,3,4]))

# Dict Inverter: Define invert_dict(d) that returns a new dict where keys and values are swapped.
def  invert_dict(d):
    return {key:value for value ,key in d.items()}
original={"a":1,"b":2}
inverted=invert_dict(original)
print(inverted)

# Set Intersection: Write a function common_elements(set1, set2) that returns their intersection.
def common_elements(set1,set2):
    result=set1&set2
    return result
print(common_elements({1,2,3,4},{3,4,5,6}))

# Tuple Converter: Define a function list_to_tuple(lst) that converts a list into a tuple.
def list_to_tuple(lst):
    return tuple(lst)
print(list_to_tuple([1,2,3,4]))
'''
# Dict Search: Write find_key(d, value) that returns the key matching the given value in a dictionary.
def find_key(d,value):
    s={"a":10,"b":20}
    for key , val in d.items():
        if val==value:
            return key
    return None
print(find_key(s,10))
# **********
'''
# List Filter Function: Define filter_even(numbers) that returns a list of even numbers only.
def filter_even(numbers):
    return[i for i in numbers if i%2==0]
print(filter_even([1,2,3,4,5,6]))


# Longest String: Write a function longest_word(words) that returns the word with the maximum length.
def longest_word(words):
    return max(words,key=len)
print (longest_word(["banana","olama","nok"]))

# Merge Dictionaries: Define a function merge_dicts(d1, d2) that combines both into one dictionary.

def merge_dicts(d1,d2):
    s=d1.copy()
    s=d1.update(d2)
    return s


# Unique Count: Write unique_count(lst) that returns how many unique elements are in the list.
def unique_count(lst):
    return len(set(lst))
print(unique_count([1,1,2,23,3,3,4]))