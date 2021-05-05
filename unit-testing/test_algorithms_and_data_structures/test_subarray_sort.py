import unittest

from algorithms_and_data_structures.arrays.subarray_sort import subarray_sort


class TestLongestPeak(unittest.TestCase):
    def test_longest_peak(self):
        self.assertEqual(subarray_sort([1, 2, 3, 4, 5, 7, 6]), [5, 6])
        self.assertEqual(subarray_sort([0, 0, 0, 0, 0, 0, 1, -1]), [0, 7])
        self.assertEqual(subarray_sort([0, 0, 0, 1, 0, 0, 1]), [3, 5])
        self.assertEqual(subarray_sort([0, 0, 0, 0, 0]), [-1, -1])
        self.assertEqual(subarray_sort([]), [-1, -1])

    def test_invalid_array(self):
        self.assertRaises(TypeError, subarray_sort, {1: 2, 2: 3})
        self.assertRaises(TypeError, subarray_sort, None)
        self.assertRaises(TypeError, subarray_sort, 1)
        self.assertRaises(TypeError, subarray_sort, ["0", "1", "3"])
