numbers_dictionary = {
    "1": [f"{number}" * number for number in range(4)],
    "2": [f"{number}" * number for number in range(3)],
    "3": [f"{number}" * number for number in range(7)],
    "4": [f"{number}" * number for number in range(5)],
    "5": [f"{number}" * number for number in range(3)],
    "6": [f"{number}" * number for number in range(6)],
    "7": [f"{number}" * number for number in range(7)],
    "8": [f"{number}" * number for number in range(10)],
    "9": [f"{number}" * number for number in range(5)],
}
print(numbers_dictionary)
# sorting the dictionary by the length of their list of values
# last_item = lambda value: value[-1]
numbers_dictionary = sorted(numbers_dictionary, key = numbers_dictionary.get)
print(numbers_dictionary)
dict2 = {
    "1": 1,
    "2": 2,
    "11": 11,
    "3": 3,
    "18": 18,
    "4": 4}

sorted_dict2 = sorted(dict2.items(), key = lambda x: x[1])

print(sorted_dict2)
min_dict2 = sorted(dict2.items(), key = lambda x: x[1])[0]
max_dict2 = sorted(dict2.items(), key = lambda x: x[1])[-1]
print(f"min in dict2: key: {min_dict2[0]}, value: {min_dict2[1]}")
print(f"max in dict2:key: {max_dict2[0]}, value: {max_dict2[1]}")

import operator

dict3 = {
    "1": 1,
    "2": 2,
    "11": 11,
    "3": 3,
    "18": 18,
    "4": 4,
    "99": 99,
    "120": 120}
# sort the dict by value
sorted_values_dict3 = sorted(dict3.items(), key = operator.itemgetter(1))
print(sorted_values_dict3)

# To sort the dict by the key:  it will sort them by the first digit/char of the key string
sorted_keys_dict3 = sorted(dict3.items(), key = operator.itemgetter(0))
print(f"sorted by the first digit/char of the key string{sorted_keys_dict3}")