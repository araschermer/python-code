# Context
# Given a  2D Array, :
#
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# We define an hourglass in A to be a subset of values with indices falling in this pattern
# in A's graphical representation:
# a b c
#   d
# e f g
# There are 16 hourglasses in A, and an hourglass sum is the sum of an hourglass' values.
#
# Task
# Calculate the hourglass sum for every hourglass in A, then print the maximum hourglass sum.
#
# Example
# In the array shown above, the maximum hourglass sum is 7 for the hourglass in the top left corner.
# Input Format
# There are 6 lines of input, where each line contains 6 space-separated integers that describe the 2D Array A.
ROW_LENGTH = 6
# Constraints
# -9<=A[i][j]<=9
# 0<=i,j<=5
# Output Format
# Print the maximum hourglass sum in A.
from nose.tools import assert_equal


def calculate_hourglass_sum(arr: []) -> int:
    for row in array:
        if len(row) != ROW_LENGTH:
            raise IndexError("the array's shape is malformed")
        for element in row:
            if type(element) != int and type(element) != float:
                raise ValueError("Invalid array values")
    # arr = []
    #  since the hourglass consists of the sum of 7 elements in arr, each element has a minimum value of -9:
    # then the minimum hourglass sum would be -9*7
    maximum = -9 * 7
    # for _ in range(6):
    #     arr.append(list(map(int, input().rstrip().split())))
    for i in range(6):
        for j in range(6):
            if i + 2 < 6 and j + 2 < 6:
                hourglass_sum = sum(arr[i][j:j + 3]) + arr[i + 1][j + 1] + sum(arr[i + 2][j:j + 3])
                if hourglass_sum > maximum:
                    maximum = hourglass_sum

    print(maximum)
    return maximum


if __name__ == '__main__':
    # Sample Input
    # 1 1 1 0 0 0
    # 0 1 0 0 0 0
    # 1 1 1 0 0 0
    # 0 0 2 4 4 0
    # 0 0 0 2 0 0
    # 0 0 1 2 4 0
    array = [[1, 1, 1, 0, 0, 0],
             [0, 1, 0, 0, 0, 0],
             [1, 1, 1, 0, 0, 0],
             [0, 0, 2, 4, 4, 0],
             [0, 0, 0, 2, 0, 0],
             [0, 0, 1, 2, 4, 0]]
    # Sample Output
    # 19
    calculate_hourglass_sum(array)
    # Explanation
    #
    # A contains the following hourglasses:
    #
    # 1 1 1   1 1 0   1 0 0   0 0 0
    #   1       0       0       0
    # 1 1 1   1 1 0   1 0 0   0 0 0
    #
    # 0 1 0   1 0 0   0 0 0   0 0 0
    #   1       1       0       0
    # 0 0 2   0 2 4   2 4 4   4 4 0
    #
    # 1 1 1   1 1 0   1 0 0   0 0 0
    #   0       2       4       4
    # 0 0 0   0 0 2   0 2 0   2 0 0
    #
    # 0 0 2   0 2 4   2 4 4   4 4 0
    #   0       0       2       0
    # 0 0 1   0 1 2   1 2 4   2 4 0
    # The hourglass with the maximum sum (19) is:
    #
    # 2 4 4
    #   2
    # 1 2 4
    assert_equal(calculate_hourglass_sum(array), 19)
