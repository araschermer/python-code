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


# list comprehension for a 1d array
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
