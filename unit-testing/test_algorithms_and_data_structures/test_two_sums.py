from unittest import TestCase

from LeetCode.two_sum import two_sum, two_sums, two_sums_
from LeetCode.util import check_validity


class TestTwoSums(TestCase):
    # Testing two_sum implementation
    def test_two_sum_valid_solutions(self):
        nums_array = [1, 2, 3, 4, 5, 6]
        self.assertEqual(two_sum(nums_array, 10), [3, 5])
        self.assertEqual(two_sum(nums_array, 0), [])
        self.assertEqual(two_sum(nums_array, 3), [0, 1])
        self.assertIn(two_sum(nums_array, 5), [[0, 3], [1, 2]])
        self.assertIn(two_sum(nums_array, 6), [[1, 3], [0, 4]])

    def test_two_sum_invalid_arrays(self):
        nums_array = [1, 20, -10, 3, 3, 3, 33, 5, -14]
        self.assertRaises(ValueError, two_sum, nums_array, 3)

        nums_array = [1, 20, -10, 3, "number", 5]
        self.assertRaises(TypeError, two_sum, nums_array, 6)
        self.assertRaises(TypeError, two_sum, nums_array, "target")
        self.assertRaises(TypeError, two_sum, nums_array, None)

    # Testing two_sums implementation
    def test_two_sum2_valid_solutions(self):
        nums_array = [1, 2, 3, 4, 5, 6]
        self.assertIn(two_sums(nums_array, 10), [[3, 5], [5, 3]])
        self.assertEqual(two_sums(nums_array, 0), [])
        self.assertIn(two_sums(nums_array, 3), [[0, 1], [1, 0]])
        self.assertIn(two_sums(nums_array, 5), [[0, 3], [3, 0], [2, 1], [1, 2]])
        self.assertIn(two_sums(nums_array, 6), [[1, 3], [3, 1], [4, 0], [0, 4]])

    def test_two_sum2_invalid_arrays(self):
        nums_array = [1, 20, -10, 3, 3, 3, 3, 33, 5]
        self.assertRaises(ValueError, two_sums, nums_array, 6)

        nums_array = [1, 20, -10, 3, "number", 5]
        self.assertRaises(TypeError, two_sums, nums_array, 6)
        self.assertRaises(TypeError, two_sums, nums_array, "target")
        self.assertRaises(TypeError, two_sums, nums_array, None)

    # testing two_sums_ implementation
    def test_two_sum1_valid_solutions(self):
        nums_array = [1, 2, 3, 4, 5, 6]
        self.assertEqual(two_sums_(nums_array, 10), [3, 5])
        self.assertEqual(two_sums_(nums_array, 0), [])
        self.assertEqual(two_sums_(nums_array, 3), [0, 1])
        self.assertIn(two_sums_(nums_array, 5), [[0, 3], [1, 2]])
        self.assertIn(two_sums_(nums_array, 6), [[1, 3], [0, 4]])

    def test_two_sum1_invalid_arrays(self):
        nums_array = [1, 20, -10, 3, 3, 33, 5]
        self.assertRaises(ValueError, two_sums_, nums_array, 6)

        nums_array = [1, 20, -10, 3, "number", 5]
        self.assertRaises(TypeError, two_sums_, nums_array, 6)
        self.assertRaises(TypeError, two_sums_, nums_array, "target")
        self.assertRaises(TypeError, two_sums_, nums_array, None)
