from unittest import TestCase

from LeetCode.two_sum import two_sum
from algorithms_and_data_structures.linked_lists.linked_list import LinkedList


class TestNode(TestCase):
    def test_two_sum_valid_solutions(self):
        nums_array = [1, 2, 3, 4, 5, 6]
        self.assertEqual(two_sum(nums_array, 10), [3, 5])
        self.assertEqual(two_sum(nums_array, 0), [])
        self.assertEqual(two_sum(nums_array, 3), [0, 1])
        self.assertIn(two_sum(nums_array, 5), [[0, 3], [1, 2]])
        self.assertIn(two_sum(nums_array, 6), [[1, 3], [0, 4]])

    def test_two_sum_invalid_arrays(self):
        nums_array = [1, 20, -10, 3, 3, 3, 3, 33, 5]
        self.assertRaises(ValueError, two_sum, nums_array, 6)

        nums_array = [1, 20, -10, 3, "number", 5]
        self.assertRaises(TypeError, two_sum, nums_array, 6)
        self.assertRaises(TypeError, two_sum, nums_array, "target")
        self.assertRaises(TypeError, two_sum, nums_array, None)
