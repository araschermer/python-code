from util import print_linked_list, insert_list, Node


class LinkedList:
    def __init__(self):
        self.head = None

    def merge_linked_lists(self, list_to_merge):
        """returns a single linked list out of merging two single linked lists with sorted elements."""
        pointer1 = self.head
        pointer2 = list_to_merge.head
        pointer3 = None
        while pointer1 and pointer2:
            if pointer1.data < pointer2.data:
                pointer3 = pointer1
                pointer1 = pointer1.next_node
            else:  # pointer1.data < pointer2.data
                if pointer3:
                    pointer3.next_node = pointer2
                pointer3 = pointer2
                pointer2 = pointer2.next_node
                pointer3.next_node = pointer1
        if pointer2:
            pointer3.next_node = pointer2
        elif pointer1:
            pointer3.next_node = pointer1
        return self if self.head.data < list_to_merge.head.data else list_to_merge

    def recursive_merge(self, list_to_merge):
        pointer1 = self.head
        pointer2 = list_to_merge.head
        print_linked_list(self)
        list_to_merge.print_linked_list()
        self.recursive_call(pointer1, pointer2)
        return self if self.head.data < list_to_merge.head.data else list_to_merge

    def recursive_call(self, pointer1, pointer2, pointer3=None):
        print_linked_list(self)
        if not pointer1:
            pointer3.next_node = pointer2
            return
        if not pointer2:
            return
        if pointer1.data < pointer2.data:
            self.recursive_call(pointer1.next_node, pointer2, pointer1)
        else:
            if pointer3 is not None:
                pointer3.next_node = pointer2
            temp_pointer2 = pointer2.next_node
            pointer2.next_node = pointer1
            self.recursive_call(pointer1=pointer1, pointer2=temp_pointer2, pointer3=pointer2)


if __name__ == '__main__':
    linked_list2 = LinkedList()
    insert_list(linked_list2, [-10, 1, 3, 4, 8])
    print_linked_list(linked_list2)
    linked_list3 = LinkedList()
    insert_list(linked_list3, [-1, 0, 2, 5])
    print_linked_list(linked_list3)
    # linked_list2 = linked_list2.recursive_merge(linked_list3)
    linked_list2 = linked_list2.merge_linked_lists(list_to_merge=linked_list3)
    print_linked_list(linked_list2)
