from unittest import TestCase

from algorithms_and_data_structures.linked_lists.linked_lists_util import print_linked_list, insert_list, Node
from algorithms_and_data_structures.linked_lists.linked_list import LinkedList


class TestNode(TestCase):

    def test_insert_valid_value_at_beginning(self):
        linked_list = LinkedList()
        data = 1
        linked_list.insert_at_beginning(data)
        self.assertEqual(linked_list.head.data, data)
        data = [1, "2", 3, 4, [1, 2, 3, 4], []]
        for value in data:
            linked_list.insert_at_beginning(value)
            self.assertEqual(value, linked_list.head.data)

    def test_insert_invalid_value_at_beginning(self):
        linked_list = LinkedList()
        data = None
        self.assertRaises(ValueError, linked_list.insert_at_beginning, data)

    def test_check_valid_index(self):
        linked_list = LinkedList()
        data = [1, 1, 2, 3, 4]
        for value in data:
            linked_list.insert_at_beginning(value)
        self.assertEqual(True, linked_list.check_valid_index(4))
        self.assertEqual(True, linked_list.check_valid_index(3))
        self.assertEqual(True, linked_list.check_valid_index(2))
        self.assertEqual(True, linked_list.check_valid_index(1))
        self.assertEqual(True, linked_list.check_valid_index(0))

    def test_check_invalid_index(self):
        linked_list = LinkedList()
        data = [1, 1, 2, 3, 4]
        for value in data:
            linked_list.insert_at_beginning(value)
        self.assertRaises(IndexError, linked_list.check_valid_index, 10)
        self.assertRaises(IndexError, linked_list.check_valid_index, -1)
        self.assertRaises(IndexError, linked_list.check_valid_index, 8)
        self.assertRaises(ValueError, linked_list.check_valid_index, "k")
        self.assertRaises(ValueError, linked_list.check_valid_index, None)

    def test_insert_element_at_index(self):
        linked_list = LinkedList()
        data = 1
        linked_list.insert_element_at_index(0, data)
        self.assertEqual(linked_list.head.data, data)
        data = 'k'
        linked_list.insert_element_at_index(1, data)
        self.assertEqual(linked_list.head.next_node.data, data)

        data = [1, 2, 3]
        linked_list.insert_element_at_index(2, data)
        self.assertEqual(linked_list.head.next_node.next_node.data, data)

    def test_append_element(self):
        linked_list = LinkedList()
        data = 1
        linked_list.append_element(data)
        self.assertEqual(linked_list.head.data, data)
        data = 'k'
        linked_list.append_element(data)
        self.assertEqual(linked_list.head.next_node.data, data)

        data = [1, 2, 3]
        linked_list.append_element(data)
        self.assertEqual(linked_list.head.next_node.next_node.data, data)
        self.assertIsNot(linked_list.head.next_node.next_node.data, 1)

    def test_append_list(self):
        linked_list = LinkedList()
        data = [1, 2, 3, 4]
        linked_list.append_list(data)
        pointer = linked_list.head
        for value in data:
            self.assertEqual(pointer.data, value)
            pointer = pointer.next_node
        self.assertIsNot(linked_list.head.data, data)

    def test_append_list_with_None_values(self):
        linked_list = LinkedList()
        data = [0, None, 1, 2, None, 3, 4]
        linked_list.append_list(data)
        pointer = linked_list.head
        for value in data:
            if value is not None:
                self.assertEqual(pointer.data, value)
                pointer = pointer.next_node
        self.assertIsNot(linked_list.head.next_node.data, None)
        self.assertIsNot(linked_list.head.next_node.next_node.next_node.next_node.data, None)
        #  inserting list containing only none value to an empty linked list
        linked_list = LinkedList()
        data = [None]
        self.assertRaises(ValueError,linked_list.append_list, data)
        self.assertEqual(linked_list.head, None)

    def test_append_empty_list(self):
        linked_list = LinkedList()
        data = []
        self.assertRaises(ValueError, linked_list.append_list, data)

    def test_get_list_length(self):
        linked_list = LinkedList()
        data = [0, None, 1, 2, None, 3, 4]
        linked_list.append_list(data)
        self.assertEqual(linked_list.get_list_length(), 5)
        self.assertIsNot(linked_list.get_list_length(), None)
        self.assertIsNot(linked_list.get_list_length(), 7)
        self.assertIsNot(linked_list.get_list_length(), 0)