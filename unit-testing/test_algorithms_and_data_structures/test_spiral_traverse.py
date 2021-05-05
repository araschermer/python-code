from unittest import TestCase

from algorithms_and_data_structures.arrays.spiral_traverse import spiral_traverse


class TestSpiralTraverse(TestCase):
    def test_spiral_traverse(self):
        self.assertEqual(spiral_traverse([[]]),
                         [])
        self.assertEqual(spiral_traverse([[1, 1, 1, 1]]),
                         [1, 1, 1, 1])
        self.assertEqual(spiral_traverse([[1, 1, 1, 1],
                                          [2, 2, 2, 2]]),
                         [1, 1, 1, 1, 2, 2, 2, 2])

        self.assertEqual(spiral_traverse([[1, 2, 3, 4],
                                          [12, 13, 14, 5],
                                          [11, 16, 15, 6],
                                          [10, 9, 8, 7]]),
                         [i for i in range(1, 17)])

    def test_string_spiral_traverse(self):
        self.assertEqual(spiral_traverse([[letter for letter in 'hello']]),
                         [letter for letter in 'hello'])
        self.assertEqual(spiral_traverse([['hello']]),
                         ['hello'])

        self.assertEqual(spiral_traverse([[1, 1, 1, 1],
                                          ['3', 2, '2', 2]]),
                         [1, 1, 1, 1, 2, '2', 2, '3'])
    def test_invalid_array(self):
        self.assertRaises(TypeError, spiral_traverse, {1: 2, 2: 3})
        self.assertRaises(TypeError, spiral_traverse, None)
        self.assertRaises(TypeError, spiral_traverse, [1, 2, 3, 4])
