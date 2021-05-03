def spiral_traverse(array: []) -> []:
    if type(array) is not list:
        raise TypeError('Invalid array type')
    for row in array:
        if type(row) is not list:
            raise TypeError('Invalid 2D array')
    result = []
    top_row = 0
    bottom_row = len(array) - 1
    left_column = 0
    right_column = len(array[0]) - 1
    # Direction is 0: move from right to left, 1: top to bottom,
    # 2: right to left, 3: bottom to top
    direction = 0
    while top_row <= bottom_row and left_column <= right_column:
        if direction == 0:

            for element in array[top_row][left_column:right_column + 1]:
                result.append(element)
            top_row += 1
        elif direction == 1:
            for row in array[top_row:bottom_row + 1]:
                result.append(row[right_column])
            right_column -= 1
        elif direction == 2:
            for element in reversed(array[bottom_row][left_column:right_column + 1]):
                result.append(element)
            bottom_row -= 1
        elif direction == 3:
            for row in reversed(array[top_row:bottom_row + 1]):
                result.append(row[left_column])
            left_column += 1
        direction = (direction + 1) % 4
    return result
