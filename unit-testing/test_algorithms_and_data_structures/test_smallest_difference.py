from unittest import TestCase
from algorithms_and_data_structures.arrays.smallest_difference import smallest_difference


class TestSmallestDifference(TestCase):
    def test_smallest_difference(self):
        self.assertEqual(smallest_difference([-1, 5, 10, 30, 28, 2], [27, 122, 160, 13, 17]), [28, 27])
        self.assertEqual(smallest_difference([-1, 5, 13, 10, 30, 28, 2], [27, 122, 160, 13, 17]), [13, 13])
        self.assertEqual(smallest_difference([-1, 5, 10, -13, 28, 2], [27, 122, 160, 13, 17]), [28, 27])
        self.assertEqual(smallest_difference([-1, 5, 10, float('-inf'), 28, 2], [27, 122, 160, 13, 17]), [28, 27])
        self.assertEqual(smallest_difference([-1, 5, 10, float('inf'), 28, 2], [27, 122, 160, 13, 17]), [28, 27])
        self.assertIsNot(smallest_difference([-1, 5, 10, 30, 28, -160, 2], [27, 122, 160, 13, 17]), [-160, 160])

    def test_invalid_nums(self):
        self.assertRaises(TypeError, smallest_difference, None, [])
        self.assertRaises(TypeError, smallest_difference, [], [])
        self.assertRaises(TypeError, smallest_difference, [1, 20, -10, 3, "number", 5], [])
        self.assertRaises(TypeError, smallest_difference, [1, 20, -10, 3, "number", 5], None)
        self.assertRaises(TypeError, smallest_difference, [1, 20, -10, 3, "number", 5], [1])
