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
    linked_list.head = Node(data=data[0])
    pointer = linked_list.head
    for element in data[1:]:
        pointer.next_node = Node(data=element)
        pointer = pointer.next_node
    return linked_list
