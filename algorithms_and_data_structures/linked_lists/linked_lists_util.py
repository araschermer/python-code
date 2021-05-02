class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


def print_linked_list(list_to_print):
    """prints the elements of a linked list"""
    if list_to_print.head is None:
        print("Linked list is Empty")
        return
    pointer = list_to_print.head
    list_as_string = ""
    while pointer is not None:
        list_as_string += f"{pointer.data}"
        if pointer.next_node is not None:
            list_as_string += " --> "
        pointer = pointer.next_node
    print(list_as_string)


def insert_list(linked_list, data: []):
    """inserts a list of elements after a given index in the linked list"""
    if data:
        pointer = linked_list.head
        for element in data:
            if element is not None:
                if pointer is None:
                    pointer = Node(data=element)
                    linked_list.head = pointer
                else:
                    pointer.next_node = Node(data=element)
                    pointer = pointer.next_node
            else:
                continue
    else:
        linked_list.head = Node(data=data)
    print_linked_list(linked_list)
    return linked_list

