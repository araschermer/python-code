from util import Node, print_linked_list, insert_list


class LinkedList:
    def __init__(self):
        self.head = None

    def detect_loop(self):
        # create two pointers both start from the beginning of the linked list
        #  pointer 1 started from the head
        pointer1 = self.head
        #  pointer two pointing at two positions after pointer 1
        pointer2 = self.head.next_node
        pointer2 = pointer2.next_node
        while pointer1 is not pointer2 and pointer2 is not None:
            pointer1 = pointer1.next_node
            pointer2 = pointer2.next_node.next_node
        #  after ending the loop, either pointer 2 points at none, with that there is no loop is detected
        #  or pointer 2 points at  the same position  as pointer 1, which mean a loop is detected
        return pointer2 is not None

    def detect_loop2(self):
        """Returns true is a loop is detected in the linked list."""
        #  Another way to  detect a loop is to store the  nodes in a list/set
        #  and check each new node against the existing nodes in the set/list
        #  if node already exists, then there's a loop
        pointer = self.head
        nodes = set()
        while pointer:
            if pointer not in nodes:
                nodes.add(pointer)
            else:
                return True
            pointer = pointer.next_node


if __name__ == "__main__":
    linked_list = LinkedList()
    insert_list(linked_list, ['A', 'B', 'C', 'D'])

    # Create a loop for testing
    linked_list.head.next_node.next_node.next_node.next_node = linked_list.head

    if linked_list.detect_loop2():
        print("Loop found")
    else:
        print("No Loop ")

    if linked_list.detect_loop():
        print("Loop found")
    else:
        print("No Loop ")
