from unittest import TestCase
from algorithms_and_data_structures.monotonic_array import monotonic_array


class TestMonotonicArray(TestCase):
    def test_monotonic_array(self):
        self.assertEqual(monotonic_array([-1, -5, -10, -100, float('-inf')]), True)
        self.assertEqual(monotonic_array([-1, -5, -10, -100]), True)
        self.assertEqual(monotonic_array([1, 2, 3, 4, 4, 5, 6]), True)
        self.assertEqual(monotonic_array([1, 2, 3, 4, 5, -1]), False)
        self.assertEqual(monotonic_array([-1, 1, 2, 3, 4, 5]), True)
        self.assertEqual(monotonic_array([-1, 1, 2, 3, 4, 5, float('inf')]), True)
        self.assertEqual(monotonic_array([1, -2, 3, 4, 5]), False)
        self.assertEqual(monotonic_array([1, 2, -3, 4, 5]), False)
        self.assertEqual(monotonic_array([1, 2, 3, -4, 5]), False)
        self.assertEqual(monotonic_array([1, 2, 3, 4, -5]), False)
        self.assertEqual(monotonic_array([]), True)
        self.assertEqual(monotonic_array([1]), True)
        self.assertEqual(monotonic_array([1, 1]), True)
        self.assertEqual(monotonic_array([1, 1, 1]), True)
        self.assertEqual(monotonic_array([1, 2]), True)
        self.assertEqual(monotonic_array([2, 1]), True)
        self.assertEqual(monotonic_array([-1, -2]), True)
        self.assertEqual(monotonic_array([0, 10000]), True)
        self.assertEqual(monotonic_array([10000, -1999]), True)
        self.assertIsNot(monotonic_array([]), False)

    def test_invalid_array(self):
        self.assertRaises(ValueError, monotonic_array, [1, 2, 4, "5"])
        self.assertRaises(ValueError, monotonic_array, ["5"])
        self.assertRaises(ValueError, monotonic_array, [" "])
        self.assertRaises(TypeError, monotonic_array, 2)
        self.assertRaises(TypeError, monotonic_array, None)
        self.assertRaises(TypeError, monotonic_array, "")
