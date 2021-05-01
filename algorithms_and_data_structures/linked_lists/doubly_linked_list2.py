class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
        self.previous = None


class DoublyLinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def set_head(self, node: Node):
        """sets the head of the linked list to the given node.
        Runtime: O(1), Space Complexity: O(1)"""
        if not self.head:  # head is none
            self.head = node
            self.tail = node
        else:
            self.insert_before(node=self.head, node_to_insert=node)

    def set_tail(self, node: Node):
        """sets the tail of the list to the given node.
        Runtime: O(1), Space Complexity: O(1)"""
        if self.tail is None:
            self.set_head(node)
        else:
            self.insert_after(self.tail, node)

    def insert_at_position(self, position, node_to_insert: Node):
        """inserts  the given node at the given position.
        Runtime: o(position)-> O(n), Space Complexity: O(1)"""
        if position == 1:
            self.set_head(node_to_insert)
        else:
            node = self.head
            current_position = 1
            while node is not None and current_position != position:
                node = node.next_node
                current_position += 1
                if node is not None:
                    self.insert_before(node, node_to_insert)
                else:
                    self.set_tail(node_to_insert)

    def insert_before(self, node: Node, node_to_insert: Node):
        """Insert a node before a given node in the list.
        Runtime: O(1), Space Complexity: O(1)"""
        if node_to_insert == self.head:
            return
        #  if the node already exists  in the list, then the it's required to change it's position
        #  to be placed just before the given node.
        self.remove(node_to_insert)
        # A -> B  ------> node_to_insert-> A -> B
        node_to_insert.previous = node.previous
        node_to_insert.next_node = node
        # If node is the head of the list
        if node.previous is None:
            self.head = node_to_insert
        else:
            # A -> B -> C
            # to insert  node_to_insert before B
            # set the  next_node of the previous node to be node_to_insert
            node.previous.next_node = node_to_insert
        node.previous = node_to_insert

    def insert_after(self, node: Node, node_to_insert: Node):
        if node_to_insert == self.head and node_to_insert == self.tail:
            return
        self.remove(node_to_insert)
        node_to_insert.previous = node
        node_to_insert.next_node = node.next_node
        if node_to_insert.next_node is None:
            self.tail = node_to_insert
        else:
            node.previous = node_to_insert
        node.next_node = node_to_insert

    def remove(self, node: Node):
        """removes a node from the list.
        Runtime: O(1), Space complexity: O(1)."""
        if node == self.head:
            self.head = self.head.next_node
        if node == self.tail:
            self.tail = self.tail.previous
        self.remove_node_bindings(node)

    def remove_node_bindings(self, node: Node):
        """removes the pointer of a given node and updates the pointers of the surrounding nodes in the list"""
        if node.previous is not None:
            node.previous.next_node = node.next_node
        if node.next_node is not None:
            node.next_node.previous = node.previous
        node.previous = None
        node.next_node = None

    def remove_node_at_index(self, index: int):
        counter = 0
        pointer = self.head
        while counter < index:
            pointer = pointer.next_node
            counter += 1
        self.remove(pointer)

    def remove_all_nodes_with_value(self, value):
        """Remove all the nodes with the given value.
        Time Complexity: O(n), Space Complexity:O(1)"""
        node = self.head
        while node is not None:
            node_to_remove = node
            node = node.next_node
            if node_to_remove.value == value:
                self.remove(node_to_remove)

    def remove_node_with_value(self, value):
        node = self.head
        while node is not None:
            if node.value == value:
                self.remove(node)
                return
            node = node.next_node

    def contains_node_with_value(self, value):
        """Returns true if the list contains the given value.
        Runtime: O(n), Space Complexity: O(1)."""
        node = self.head
        while node is not None and node.value != value:
            node = node.next_node
        return node is not None
