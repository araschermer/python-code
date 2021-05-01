from linked_lists_util import print_linked_list, insert_list, Node


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse_linked_list(self):
        pointer1 = None
        pointer2 = self.head
        while pointer2:
            pointer3 = pointer2.next_node
            pointer2.next_node = pointer1
            pointer1 = pointer2
            pointer2 = pointer3
            if pointer2:
                self.head = pointer2
        return self


if __name__ == '__main__':
    linked_list = LinkedList()
    insert_list(linked_list, [1, 15, 1, -10, 3, 4, 8])
    print_linked_list(linked_list)
    linked_list.reverse_linked_list()
    print_linked_list(linked_list)
