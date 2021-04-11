# https://www.hackerrank.com/challenges/30-scope
# The absolute difference between two integers, and , is written as . The maximum absolute difference between two
# integers in a set of positive integers, , is the largest absolute difference between any two integers in .
# The Difference class is started for you in the editor. It has a private integer array () for storing non-negative
# integers, and a public integer () for storing the maximum absolute difference.
#
# Task
# Complete the Difference class by writing the following:
# A class constructor that takes an array of integers as a parameter and saves it to the instance variable.
# A computeDifference method that finds the maximum absolute difference
# between any 2 numbers in __elements and stores it in the  maximumDifference instance variable.

# Output  print the value of the maximumDifference instance variable.
# Sample Input
# 3 1 2 5
# Sample Output 4
# Explanation The scope of the __elements array and  maximumDifference integer is the entire class instance. The
# class constructor saves the argument passed to the constructor as the __elements instance variable (where the
# computeDifference method can access it).
#
# To find the maximum difference, computeDifference checks each element in the array and finds the maximum difference
# between any 2 elements:|1-2|=1, |1-5|=4, |2-5|=3
# The maximum of these differences is , so it saves the value 4 as the maximumDifference instance variable.
# The locked stub code in the editor then prints the value stored as maximumDifference, which is 4 .
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        self.__elements.sort()
        self.maximumDifference = abs(self.__elements[0] - self.__elements[-1])


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)