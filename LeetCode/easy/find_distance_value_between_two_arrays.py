def find_the_distance_value(arr1: [int], arr2: [int], d: int) -> int:
    """Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.
    The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where
    |arr1[i]-arr2[j]| <= d. """
    array = []  # holds the value in arr1 and not in arr2
    for i in arr1:
        var = len(arr2)  # in the beginning of the each iteration, initiate var=len(arr2)
        for j in arr2:
            if abs(i - j) > d:  # if  i and j do not fulfill |arr1[i]-arr2[j]| <= d., then subtract 1 from var
                var -= 1
            else:
                break  # element j not interesting since it fulfill arr1[i]-arr2[j]| <= d
        if var == 0:  # var=0, when element arr1[i] is not fulfilling |arr1[i]-arr2[j]|<= d. for all elements in arr2
            array.append(i)
    # return length of array which contains all the elements  from arr1
    # that fulfill the distance value formula with all elements of arr2
    return len(array)


# Example 1: Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2 Output: 2
# Explanation: For arr1[0]=4 we have: |4-10|=6 > d=2 |4-9|=5 > d=2 |4-1|=3 > d=2 |4-8|=4 > d=2
# For arr1[1]=5 we have: |5-10|=5 > d=2 |5-9|=4 > d=2 |5-1|=4 > d=2 |5-8|=3 > d=2 For arr1[2]=8
# we have: |8-10|=2 <= d=2 |8-9|=1 <= d=2 |8-1|=7 > d=2 |8-8|=0 <= d=2
assert find_the_distance_value([4, 5, 8], [10, 9, 1, 8], 2), 2
# Example 2: Input: arr1 = [1,4,2,3], arr2 = [-4,-3,6,10,20,30], d = 3 Output: 2
assert find_the_distance_value(arr1 = [1, 4, 2, 3], arr2 = [-4, -3, 6, 10, 20, 30], d = 3), 2
# Example 3: Input: arr1 = [2,1,100,3], arr2 = [-5,-2,10,-3,7], d = 6 Output: 1
assert find_the_distance_value(arr1 = [2, 1, 100, 3], arr2 = [-5, -2, 10, -3, 7], d = 6), 2

# Input arr1=[-3,10,2,8,0,10], arr2=[-9,-1,-4,-9,-8], d=9, output=2
assert find_the_distance_value(arr1 = [-3, 10, 2, 8, 0, 10], arr2 = [-9, -1, -4, -9, -8], d = 9), 2
