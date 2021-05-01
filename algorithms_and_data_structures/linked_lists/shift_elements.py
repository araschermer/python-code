from util import print_linked_list, insert_list


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
            self.set_head(head=old_tail)
            # repeat number of shifts times to get all elements of the list shifted by the given number of shifts
        return self

    def get_tail(self):
        pointer = self.head
        while pointer.next_node:
            pointer = pointer.next_node
        return pointer

    def set_head(self, head):
        pointer = self.head
        self.head = head
        self.head.next_node = pointer
        return self

    def remove_tail(self):
        pointer = self.head
        while pointer.next_node.next_node:
            pointer = pointer.next_node
        pointer.next_node = None
        return self


if __name__ == '__main__':
    linked_list2 = LinkedList()
    insert_list(linked_list2, [-10, 3, 2, 10, 1, 3, -5, 4, 3, 8, 0])
    print_linked_list(linked_list2)
    linked_list2 = linked_list2.shift_elements(3)
    print_linked_list(linked_list2)
