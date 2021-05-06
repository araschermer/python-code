def out_of_bounds(row, column, height, width) -> bool:
    return row < 0 or row > height or column < 0 or column > width


def zigzag_traverse(array: []) -> []:
    height = len(array) - 1
    width = len(array[0]) - 1
    result = []
    row = 0
    column = 0
    go_diagonally_down = True
    while not out_of_bounds(row, column, height, width):
        result.append(array[row][column])
        if go_diagonally_down:
            column, go_diagonally_down, row = go_diagonal(column, go_diagonally_down, height, row)
        else:
            if row == 0 or column == width:
                go_diagonally_down = True
                if column == width:
                    row += 1
                else:
                    column += 1
            else:
                row -= 1
                column += 1
    return result


def go_diagonal(column, go_diagonally_down, height, row):
    if column == 0 or row == height:
        go_diagonally_down = False
        if row == height:
            column += 1
        else:
            row += 1
    else:
        row += 1
        column -= 1
    return column, go_diagonally_down, row


print(zigzag_traverse([[1, 2, 3, 10],
                       [2, 5, 9, 11],
                       [6, 8, 12, 15],
                       [7, 13, 14, 16]]))
