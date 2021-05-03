from unittest import TestCase

from algorithms_and_data_structures.move_element_to_end import move_elements_to_end


class TestMoveElementsToEnd(TestCase):
    def test_move_elements_to_end(self):
        self.assertEqual(move_elements_to_end([2, 1, 2, 2, 2, 3, 4, 2], 2), [4, 1, 2, 3, 2, 2, 2, 2])
        self.assertEqual(move_elements_to_end([1, 1, 1, 1, 1, 19, 1, 80], 1), [80, 1, 19, 1, 1, 1, 1, 1])
        self.assertEqual(move_elements_to_end([0, 1, None, 1, 0, 19, 1, 80], 0), [80, 1, None, 1, 1, 19, 0, 0])
        self.assertEqual(move_elements_to_end(['a', 1, 'a', 'a', 1, 19, 1, 80], 'a'), [80, 1, 1, 19, 1, 'a', 'a', 'a'])
        self.assertEqual(move_elements_to_end(['a'], 'a'), ['a'])
        self.assertEqual(move_elements_to_end(['a', ['a', 'a']], 'a'), [['a', 'a'], 'a'])
        self.assertEqual(move_elements_to_end(['a', ['a', 'a']], ['a', 'a']), ['a', ['a', 'a']])
        self.assertEqual(move_elements_to_end([], []), [])

    def test_not_valid_values(self):
        self.assertRaises(ValueError, move_elements_to_end, [1, 2, 3, 4], 0)
        self.assertRaises(TypeError, move_elements_to_end, [1, 2], None)
        self.assertRaises(ValueError, move_elements_to_end, ['a', ['a']], ['a', 'a'])
