from linked_lists_util import print_linked_list, insert_list


class LinkedList:
    def __init__(self):
        self.head = None

    def rearrange_list(self, pivot):
        """rearranging the list around a given node in the list,
        returns a list with nodes that contains values smaller than the value of the pivot to the left  of the pivot,
        and  the nodes that contain values greater than the value of the pivot to the right of the pivot.
        all elements but the pivot should preserve there order."""
        bigger_values = []
        smaller_values = []
        pivots = []
        pointer = self.head
        while pointer is not None:
            if pointer.data > pivot:
                bigger_values.append(pointer)
            elif pointer.data < pivot:
                smaller_values.append(pointer)
            else:
                pivots.append(pointer)
            pointer = pointer.next_node
        pointer = smaller_values[0]
        self.head = pointer
        # print(pointer.data)
        result = ""
        for node in smaller_values[1:]:
            result += str(node.data) + " -> "
            pointer.next_node = node
        for node in pivots:
            result += str(node.data) + " -> "
            pointer.next_node = node
        for index, node in enumerate(bigger_values):
            result += str(node.data)
            if index < len(bigger_values) - 1:
                result += " -> "
            pointer.next_node = node
        print(result)

    def rearrange_list2(self, pivot):
        pivots_tail = smaller_values_tail = bigger_values_tail = None
        pivots_head = smaller_values_head = bigger_values_head = None
        pointer = self.head
        while pointer:
            if pointer.data == pivot:
                pivots_head, pivots_tail = self.grow_list(pointer, pivots_head, pivots_tail)
            elif pointer.data > pivot:
                # print(pointer.data)
                bigger_values_head, bigger_values_tail = self.grow_list(pointer, bigger_values_head,
                                                                        bigger_values_tail)
            else:
                smaller_values_head, smaller_values_tail = self.grow_list(pointer, smaller_values_head,
                                                                          smaller_values_tail)
            temp = pointer
            pointer = pointer.next_node
            temp.next_node = None
        self.head = pivots_head
        self.connect_lists(bigger_values_head, pivots_head, pivots_tail, smaller_values_head, smaller_values_tail)
        return self

    def connect_lists(self, bigger_values_head, pivots_head, pivots_tail, smaller_values_head, smaller_values_tail):
        if smaller_values_head:
            self.head = smaller_values_head
            smaller_values_tail.next_node = pivots_head
        if bigger_values_head:
            pivots_tail.next_node = bigger_values_head
        print(self.head.data)

    def grow_list(self, pointer, list_head, list_tail):
        # if pointer and list_head and list_tail:
        #     print(pointer.data, list_head.data, list_tail.data)
        new_head = list_head
        new_tail = pointer
        if not new_head:
            new_head = pointer
        if list_tail:
            list_tail.next_node = pointer
        return new_head, new_tail


if __name__ == '__main__':
    linked_list2 = LinkedList()
    insert_list(linked_list2, [-10, 3, 2, 10, 1, 3, -5, 4, 3, 8, 0])
    print_linked_list(linked_list2)
    # linked_list = linked_list2.rearrange_list(3)
    linked_list2 = linked_list2.rearrange_list2(3)
    print_linked_list(linked_list2)
