from unittest import TestCase

from LeetCode.three_sum import three_sum


class TestThreeSum(TestCase):
    def test_valid_nums(self):
        array = [9, 2, 1, 3, 3, -6, 5, -8, 6]
        self.assertEqual(three_sum(array), [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5], [-6, 3, 3]])
        self.assertEqual(three_sum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]])
        self.assertEqual(three_sum([]), [])
        self.assertEqual(three_sum([0]), [])
        self.assertEqual(three_sum([0, 1]), [])
        self.assertEqual(three_sum([0, 1, 3]), [])
        self.assertEqual(three_sum([0, 0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(three_sum([0, 0, 0]), [[0, 0, 0]])
        self.assertEqual(three_sum([-2, 0, 1, 1, 2]), [[-2, 0, 2], [-2, 1, 1]])

    def test_invalid_nums(self):
        self.assertRaises(TypeError, three_sum, None, [])
        nums_array = [1, 20, -10, 3, "number", 5]
        self.assertRaises(TypeError, three_sum, nums_array)
