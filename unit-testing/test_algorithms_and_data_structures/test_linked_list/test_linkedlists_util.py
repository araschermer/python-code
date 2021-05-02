from unittest import TestCase
from algorithms_and_data_structures.linked_lists.linked_lists_util import print_linked_list, insert_list, Node
from algorithms_and_data_structures.linked_lists.linked_list import LinkedList


class TestNode(TestCase):

    def test_node_creation(self):
        data = "string"
        node = Node(data)
        self.assertEqual(node.data, data)
        data = [1, 2, 3, 4]
        node = Node(data)
        self.assertEqual(node.data, data)
        # Data is empty list
        data = []
        node = Node(data)
        self.assertEqual(node.data, data)
        # data is None
        data = None
        node = Node(data)
        self.assertEqual(node.data, None)
        data = False
        node = Node(data)
        self.assertEqual(node.data, data)
        data = True
        node = Node(data)
        self.assertEqual(node.data, data)


class TestListInsertion(TestCase):
    def test_list_insertion(self):
        linked_list = LinkedList()
        nodes_data = [1, 2, 3, 4, 5]
        insert_list(linked_list, nodes_data)
        pointer = linked_list.head
        if nodes_data:
            for data in nodes_data:
                self.assertEqual(data, pointer.data)
                pointer = pointer.next_node
        else:
            self.test_empty_list_insertion(nodes_data)

    def test_empty_list_insertion_with_lists_containing_none_values(self):
        linked_list = LinkedList()
        nodes_data = [1, None, 2, 3, None, None, 4, 5]
        insert_list(linked_list, nodes_data)
        pointer = linked_list.head
        for data in nodes_data:
            if data is not None:
                self.assertEqual(data, pointer.data)
                pointer = pointer.next_node

    def test_empty_list_insertion(self, nodes_data=[]):
        linked_list = LinkedList()
        insert_list(linked_list, nodes_data)
        self.assertEqual([], linked_list.head.data)


from unittest.mock import patch


class TestPrintingList(TestCase):
    @patch('builtins.print')
    def test_print_linked_list_with_none_values(self, mock_print):
        linked_list = LinkedList()
        nodes_data = [1, None, 2, 3, None, None, 4, 5]
        insert_list(linked_list, nodes_data)
        print_linked_list(linked_list)
        mock_print.assert_called_with('1 --> 2 --> 3 --> 4 --> 5')

    @patch('builtins.print')
    def test_print_linked_list(self, mock_print):
        linked_list = LinkedList()
        nodes_data = [1, 2, 3, 4, 5]
        insert_list(linked_list, nodes_data)
        print_linked_list(linked_list)
        mock_print.assert_called_with('1 --> 2 --> 3 --> 4 --> 5')

    @patch('builtins.print')
    def test_print_empty_linked_list(self, mock_print):
        linked_list = LinkedList()
        nodes_data = []
        insert_list(linked_list, nodes_data)
        print_linked_list(linked_list)
        mock_print.assert_called_with('[]')
