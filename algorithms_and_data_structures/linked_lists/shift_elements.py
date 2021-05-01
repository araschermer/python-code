from util import print_linked_list, insert_list, Node


class LinkedList:
    def __init__(self):
        self.head = None

    def shift_elements(self, shifts):
        """Shift the elements of the linked list by a given number of shifts."""
        for _ in range(shifts):
            #  get the current tail of the list
            old_tail = self.get_tail()
            #  delete the current tail
            self.remove_tail()
            # place the current tail in the  beginning of the list, with that all elements of the list  get shifted
            # by one
            self.set_head(new_head=old_tail)
            # repeat number of shifts times to get all elements of the list shifted by the given number of shifts
        return self

    def get_tail(self):
        """returns the last node in the linked list."""
        pointer = self.head
        while pointer.next_node:
            pointer = pointer.next_node
        return pointer

    def set_head(self, new_head: Node):
        """sets a new head of the linked list to be the given node"""
        pointer = self.head
        self.head = new_head
        self.head.next_node = pointer
        return self

    def remove_tail(self):
        """removes the last element from the linked list"""
        pointer = self.head
        while pointer.next_node.next_node:
            pointer = pointer.next_node
        pointer.next_node = None
        return self

    def shift_elements2(self, num_shifts: int):
        """Shifts all the elements of the list by the number of shifts given as parameters.
        :param num_shifts: The number of shifts to shift the elements of the list by. positive integer"""
        length = self.get_length()
        if num_shifts == 0:
            return self
        pointer = self.head
        tail_position = length - num_shifts
        for _ in range(tail_position - 1):
            pointer = pointer.next_node
        new_tail = pointer
        new_head = new_tail.next_node
        new_tail.next_node = None
        head = new_head
        for _ in range(num_shifts - 1):
            new_head = new_head.next_node
        new_head.next_node = self.head
        self.head = head
        return self

    def get_length(self):
        """Returns length of the linked list."""
        pointer = self.head
        counter = 0
        while pointer:
            counter += 1
            pointer = pointer.next_node
        return counter


if __name__ == '__main__':
    linked_list2 = LinkedList()
    insert_list(linked_list2, [-10, 3, 2, 10, 1, 3, -5, 4, 3, 8, 0])
    print(linked_list2.get_length())
    print_linked_list(linked_list2)
    # linked_list2 = linked_list2.shift_elements(3)
    # print_linked_list(linked_list2)
    linked_list2 = linked_list2.shift_elements2(3)
    print_linked_list(linked_list2)
