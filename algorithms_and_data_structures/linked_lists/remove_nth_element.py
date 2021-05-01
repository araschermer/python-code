from util import print_linked_list, insert_list, Node


class LinkedList:
    def __init__(self):
        self.head = None

    def remove_nth_node_from_end(self, n: int):
        """Removes the node at the nth position from the end of the linked list."""
        pointer1 = self.head
        pointer2 = self.head
        for _ in range(n + 1):
            #  move the second pointer to be distant by n+1 positions from the first pointer
            pointer2 = pointer2.next_node
        # move the second pointer to the end of the list
        while pointer2 is not None:
            pointer2 = pointer2.next_node
            pointer1 = pointer1.next_node
        # after the while loop , pointer 2 is pointing at none
        # and pointer 1 is at  element before the nth  position from the end of the linked list
        #  remove the element at the nth position from the list
        temp = pointer1.next_node
        pointer1.next_node = None
        pointer1.next_node = temp.next_node
        return self


if __name__ == '__main__':
    linked_list = LinkedList()
    insert_list(linked_list, [1, 1, 1, 1, 1, 1, 1, 1, -10, 'element_to_remove', 3, 4, 8])
    print_linked_list(linked_list)
    linked_list.remove_nth_node_from_end(4)
    print_linked_list(linked_list)
