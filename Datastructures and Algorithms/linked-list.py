class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """inserts an element at the beginning of the linked list.
        :param data : the data of the new node"""
        # initializing a node object with given data and the next node of the current head
        node = Node(data, self.head)
        # update the head to point at the new node
        # The structure should look like:  New_new (head) -> node (old_head, which might be null)
        self.head = node

    def check_valid_index(self, index):
        """checks if a given index is valid, otherwise raises an index error"""
        list_length = self.get_list_length()
        if 0 > index or index > list_length:
            raise IndexError("This Index is out of bounds")

    def insert_element_at_index(self, index, data):
        """inserts an element at a given index in a linked list."""
        self.check_valid_index(index)
        if index == 0:
            self.insert_at_beginning(data)
            return
        counter = 0
        pointer = self.head
        while pointer:
            if counter == index - 1:
                pointer.next_node = Node(data, pointer.next_node)
                return
            counter += 1
            pointer = pointer.next_node

    def append_element(self, data):
        """inserts an element at the end of a linked list"""
        if self.head is None:
            self.head = Node(data, None)
            return
        pointer = self.head
        while pointer.next_node is not None:
            pointer = pointer.next_node
        pointer.next_node = Node(data, None)

    def append_list(self, data_list):
        """inserts a list at the end of a linked list"""
        for data in data_list:
            self.append_element(data)

    def get_list_length(self):
        """returns the length of the linked list"""
        counter = 0
        pointer = self.head
        while pointer:
            counter += 1
            pointer = pointer.next_node
        return counter

    def insert_list_starting_index(self, index, data: []):
        """inserts a list of elements after a given index in the linked list"""
        for i, element in enumerate(data):
            self.insert_element_at_index(index + i, element)

    def remove_element_at_index(self, index):
        """remove element at a given index from the linked list"""
        self.check_valid_index(index)
        if index == 0:
            self.head = self.head.next_node
        counter = 0
        pointer = self.head
        while pointer is not None:
            if counter == index - 1:
                pointer.next_node = pointer.next_node.next_node
                break
            pointer = pointer.next_node
            counter += 1

    def insert_after_value(self, value, data):
        """inserts an element after another element of a given value."""
        pointer = self.head
        while pointer is not None:
            if pointer.data == value:
                pointer.next_node = Node(data, pointer.next_node)
                return
            pointer = pointer.next_node

    def remove_by_value(self, value):
        """removes an element of a given value from the linked list."""
        if not self.head:
            return
        pointer = self.head
        while pointer.next_node is not None:
            if pointer.next_node.data == value:
                # pointer: node_x -> node_to_delete -> node_y
                #  node_x -> node_y
                pointer.next_node = pointer.next_node.next_node
                return
            pointer = pointer.next_node

    def get_tail(self):
        pointer = self.head
        while pointer.next_node is not None:
            pointer = pointer.next_node
        return pointer

    def print_linked_list(self):
        """prints the elements of a linked list"""
        if self.head is None:
            print("Linked list is Empty")
            return
        pointer = self.head
        list_as_string = ""
        while pointer is not None:
            list_as_string += f"{pointer.data}"
            if pointer.next_node is not None:
                list_as_string += " --> "
            pointer = pointer.next_node
        print(list_as_string)

    def print_reversed_list(self):
        """prints the elements of a linked list in a reverse order"""
        if self.head is None:
            print("Linked list is Empty")
            return
        pointer = self.get_tail()
        list_as_string = ""
        while pointer is not None:
            list_as_string += f"{pointer.data}"
            if pointer.next_node is not None:
                list_as_string += " --> "
            pointer = pointer.next_node
        print(list_as_string)


if __name__ == "__main__":
    linked_list = LinkedList()
    linked_list.insert_at_beginning(10)
    linked_list.insert_at_beginning(100)
    linked_list.insert_at_beginning(1000)
    linked_list.append_element(0)
    linked_list.append_list([1, 2, 3, 4, 5])
    # 1000 --> 100 --> 10 --> 0 --> 1 --> 2 --> 3 --> 4 --> 5
    linked_list.print_linked_list()

    print(linked_list.get_list_length())  # 9
    linked_list.remove_element_at_index(2)
    # 1000 --> 100 --> 0 --> 1 --> 2 --> 3 --> 4 --> 5
    linked_list.print_linked_list()
    linked_list.insert_element_at_index(3, 99)
    # 1000 --> 100 --> 0 --> 99 --> x --> y --> z --> 1 --> 2 --> 3 --> 4 --> 5
    linked_list.print_linked_list()
    linked_list.insert_list_starting_index(4, ["x", "y", "z"])
    # 100 --> 0 --> 99 --> x --> y --> z --> 1 --> 2 --> 3 --> 4 --> 5
    linked_list.print_linked_list()
    linked_list.remove_element_at_index(0)
    # 100 --> 0 --> 99 --> x --> y --> z --> 1 --> 2 --> 3 --> 4 --> 5
    linked_list.print_linked_list()
    linked_list.insert_after_value("x", 9999999)
    # 100 --> 0 --> 99 --> x --> 9999999 --> y --> z --> 1 --> 2 --> 3 --> 4 --> 5
    linked_list.print_linked_list()
    linked_list.remove_by_value("z")
    # 100 --> 0 --> 99 --> x --> 9999999 --> y --> z --> 1 --> 2 --> 3 --> 4 --> 5
    linked_list.print_linked_list()
    print(f"tail value = {linked_list.get_tail().data}")
