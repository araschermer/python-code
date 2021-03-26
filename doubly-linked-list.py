class Node:
    def __init__(self, data, next_node=None, previous=None):
        self.data = data
        self.next_node = next_node
        self.previous = previous


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        if self.head is None:
            print(data)
            self.head = Node(data)
            return
        self.head = Node(data, self.head, self.head.previous)

    def append_element(self, data):
        if self.head is None:
            #  the new node with value data will be the new head,
            #  the next and previous nodes are null, since the list contains only one element.
            self.head = Node(data)
            return
        pointer = self.head
        while pointer.next_node:
            pointer = pointer.next_node
        pointer.next_node = Node(data, previous=pointer, next_node=None)

    def get_list_length(self):
        counter = 0
        pointer = self.head
        while pointer:
            counter += 1
            pointer = pointer.next_node
        return counter

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

    def insert_list_starting_index(self, index, data_list: []):
        for index_, node in enumerate(data_list):
            self.insert_element_at_index(data=node, index=(index + index_))

    def get_tail(self):
        pointer = self.head
        while pointer.next_node:
            pointer = pointer.next_node
        tail = pointer
        return tail

    def print_forwards(self):
        if self.head is None:
            print("List is empty")
            return
        dls = ""
        pointer = self.head
        while pointer is not None:
            dls += f"{pointer.data}"
            if pointer.next_node is not None:
                dls += " --> "
            pointer = pointer.next_node
        print(dls)

    def print_reversed_linked_list(self):
        reversed_dls = ""
        pointer = None
        while self.get_tail() != self.head:
            pointer = self.head.next_node
            pointer.previous = self.head
            self.head = pointer
        while pointer is not None:
            reversed_dls += f"{pointer.data}"
            if pointer.previous is not None:
                reversed_dls += " --> "
            pointer = pointer.previous
        print(reversed_dls)

    def check_valid_index(self, index):
        if self.get_list_length() < index or index < 0:
            raise IndexError("Index out of bounds")
        else:
            return True


if __name__ == "__main__":
    dls = DoublyLinkedList()
    dls.insert_at_beginning(10)
    dls.insert_at_beginning(100)
    dls.insert_at_beginning(1000)
    dls.print_forwards()
    dls.append_element("k")
    print(dls.get_list_length())
    dls.print_forwards()
    print(dls.get_list_length())
    dls.print_forwards()
    dls.insert_element_at_index(data="x", index=1)
    dls.insert_element_at_index(index=1, data="y")
    dls.print_forwards()
    dls.insert_list_starting_index(data_list=["h", "b", "P"], index=3)
    dls.print_forwards()
    # dls.print_reversed_linked_list()

    # dls.print_reversed_linked_list()
    # print(f"dls.get_list_length(): {dls.get_list_length()}")
    # print(f"dls.check_valid_index(90):{dls.check_valid_index(90)}")
    # print(f"dls.check_valid_index(1):{dls.check_valid_index(1)}")
