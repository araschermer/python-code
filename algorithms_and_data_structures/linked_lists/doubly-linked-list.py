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

    def get_tail(self):
        pointer = self.head
        while pointer.next_node:
            pointer = pointer.next_node
        tail = pointer
        return tail

    def remove_element_at_beginning(self):
        if self.head is None:
            print("The list is already empty")
        elif self.head.next_node is None:
            self.head = None
        else:
            self.head = self.head.next_node
            self.head.previous = None

    def remove_last_element(self):
        pointer = self.head
        if self.head is None:
            print("The list is already empty")
        elif self.head.next_node is None:
            self.head = None

        else:
            while pointer.next_node is not None:
                pointer = pointer.next_node
            pointer.previous.next_node = None

    def print_forwards(self):
        if self.head is None:
            print("List is empty")
            return
        doubly_linked_list = ""
        pointer = self.head
        while pointer is not None:
            doubly_linked_list += f"{pointer.data}"
            if pointer.next_node is not None:
                doubly_linked_list += " --> "
            pointer = pointer.next_node
        print(doubly_linked_list)

    def reverse_linked_list(self):
        if self.head is None:
            print("The list has no element to delete")
            return
        pointer1 = self.head
        pointer2 = pointer1.next_node
        pointer1.next_node = None
        pointer1.previous = pointer2
        while pointer2 is not None:
            pointer2.previous = pointer2.next_node
            pointer2.next_node = pointer1
            pointer1 = pointer2
            pointer2 = pointer2.previous
        self.head = pointer1

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
    print("remove last element:")
    dls.remove_last_element()
    dls.print_forwards()
    dls.remove_element_at_beginning()
    print("remove first element:")
    dls.print_forwards()
    print("Reverse list")
    dls.reverse_linked_list()
    dls.print_forwards()
