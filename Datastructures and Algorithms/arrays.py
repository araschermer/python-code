# appending elements to the first unoccupied element in the array
array1 = []
for num in range(10):
    array1.append(num)

print(f"array1: {array1}")
# Inserting elements at the beginning of the array
array3 = []
for num in range(10):
    array3.insert(0, num)
print(f"array3:{array3}")

# insert number at index of the number's value
array4 = []
for num in range(10):
    array4.insert(num, num)
print(f"array4: {array4}")

# to remove item from array
array = [i for i in range(10)]
array.remove(9)
print(f"Array: {array}")
# Reverse Array
array.reverse()
print(f"Array: {array}")

# getting index of element
print(f"Index of element 5 in {array} is {array.index(5)}")
# search element between indices
array = [1, 2, 4, 1, 2, 3, 2, 1, 3, 2, 2, 1, ]
print(f"index of element 2 between indices 0,2 in {array} is {array.index(2, 0, 2)}")
# counting number of appearance of number 2 in the array
print(f"element number 2 appears {array.count(2)} times in {array}")

# list comprehension for a 1D array
flat_list = [element for element in range(4 * 4)]

# Row major 2d array
row_major_2d_array = []
start = 0
end = 4  # num of columns
for _ in range(4):  # num of rows
    row_major_2d_array.append(flat_list[start:end])
    start += 4  # num of columns
    end += 4  # num of columns
state_var = len(flat_list)  # updates the state variable to the number of elements in the matrix
print(f"row major 2d array: {row_major_2d_array}")

# Column major 2d array
column_major_2d_array = []
start = 0
for _ in range(4):
    # number of rows equals 4
    column_major_2d_array.append(flat_list[start:: 4])  # start from first element and jump by 4 to get the next element
    start += 1
print(f"Column major 2D array{column_major_2d_array}")
