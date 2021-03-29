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
