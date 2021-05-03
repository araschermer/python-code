import unittest

from algorithms_and_data_structures.longest_peak import longest_peak


class TestLongestPeak(unittest.TestCase):
    def test_longest_peak(self):
        self.assertEqual(longest_peak([0, 1, 3, 4, 4, -1, 11, 6, 5, -1, -3, 2, ]), 6)
        self.assertEqual(longest_peak([]), 0)
        self.assertEqual(longest_peak([-1, -1, 1, 3, 4, 5, 10, -1, -1, -2]), 7)

    def test_invalid_array(self):
        self.assertRaises(TypeError, longest_peak, {1: 2, 2: 3})
        self.assertRaises(TypeError, longest_peak, None)
        self.assertRaises(TypeError, longest_peak, 1)
        self.assertRaises(TypeError, longest_peak, ["0", "1", "3"])
