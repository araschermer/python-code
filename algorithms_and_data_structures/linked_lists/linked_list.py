class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """inserts an element at the beginning of the linked list.
        :param data : the data of the new node"""
        # initializing a node object with given data and the next node of the current head
        node = Node(data, self.head)
        # update the head to point at the new node
        # The structure should look like:  New_new (head) -> node (old_head, which might be null)
        self.head = node

    def check_valid_index(self, index):
        """checks if a given index is valid, otherwise raises an index error"""
        list_length = self.get_list_length()
        if 0 > index or index > list_length:
            raise IndexError("This Index is out of bounds")

    def insert_element_at_index(self, index, data):
        """inserts an element at a given index in a linked list."""
        self.check_valid_index(index)
        if index == 0:
            self.insert_at_beginning(data)
            return
        counter = 0
        pointer = self.head
        while pointer:
            if counter == index - 1:
                pointer.next_node = Node(data, pointer.next_node)
                return
            counter += 1
            pointer = pointer.next_node

    def append_element(self, data):
        """inserts an element at the end of a linked list"""
        if self.head is None:
            self.head = Node(data, None)
            return
        pointer = self.head
        while pointer.next_node is not None:
            pointer = pointer.next_node
        pointer.next_node = Node(data, None)

    def append_list(self, data_list):
        """inserts a list at the end of a linked list"""
        for data in data_list:
            self.append_element(data)

    def get_list_length(self):
        """returns the length of the linked list"""
        counter = 0
        pointer = self.head
        while pointer:
            counter += 1
            pointer = pointer.next_node
        return counter

    def insert_list_starting_index(self, index, data: []):
        """inserts a list of elements after a given index in the linked list"""
        for i, element in enumerate(data):
            self.insert_element_at_index(index + i, element)

    def remove_element_at_index(self, index):
        """remove element at a given index from the linked list"""
        self.check_valid_index(index)
        if index == 0:
            self.head = self.head.next_node
        counter = 0
        pointer = self.head
        while pointer is not None:
            if counter == index - 1:
                pointer.next_node = pointer.next_node.next_node
                break
            pointer = pointer.next_node
            counter += 1

    def insert_after_value(self, value, data):
        """inserts an element after another element of a given value."""
        pointer = self.head
        while pointer is not None:
            if pointer.data == value:
                pointer.next_node = Node(data, pointer.next_node)
                return
            pointer = pointer.next_node

    def remove_by_value(self, value):
        """removes the first element of a given value from the linked list."""
        if not self.head:
            return False
        pointer = self.head
        # if the head contains the value
        if self.head.data == value:
            self.head = self.head.next_node
            return True
        while pointer.next_node is not None:
            if pointer.next_node.data == value:
                # pointer: node_x -> node_to_delete -> node_y
                #  node_x -> node_y
                pointer.next_node = pointer.next_node.next_node
                return True
            pointer = pointer.next_node
        return False

    def remove_all_by_value(self, value):
        while self.remove_by_value(value):
            self.remove_by_value(value)

    def get_tail(self):
        """Returns the last element in the linked list."""
        pointer = self.head
        while pointer.next_node is not None:
            pointer = pointer.next_node
        return pointer

    def print_linked_list(self):
        """prints the elements of a linked list"""
        if self.head is None:
            print("Linked list is Empty")
            return
        pointer = self.head
        list_as_string = ""
        while pointer is not None:
            list_as_string += f"{pointer.data}"
            if pointer.next_node is not None:
                list_as_string += " --> "
            pointer = pointer.next_node
        print(list_as_string)

    def contains_value(self, value) -> bool:
        """Returns true is the list contains the specified value."""
        pointer = self.head
        while pointer is not None:
            if pointer.data == value:
                print(f"{value} is in the linked list ")
                return True
            pointer = pointer.next_node
        print(f"{value} is not in the linked list ")
        return False

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

    def reverse_linked_list(self):
        pointer1 = None
        pointer2 = self.head
        #  None (pointer1), A (pointer2)-> B  -> C -> D
        while pointer2 is not None:
            #  None (pointer1), A (pointer2)-> B (pointer3)  -> C -> D
            pointer3 = pointer2.next_node
            #  None (pointer1)<-A (pointer2)-> B (pointer3) -> C -> D
            pointer2.next_node = pointer1
            #  None <-A (pointer2,1) -> B  (pointer3) -> C -> D
            pointer1 = pointer2
            #  None <-A (pointer1)-> B  (pointer2,3) -> C -> D
            pointer2 = pointer3

        self.head = pointer1
        return self.head

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
        self.print_linked_list()
        list_to_merge.print_linked_list()
        self.recursive_call(pointer1, pointer2)
        return self if self.head.data < list_to_merge.head.data else list_to_merge

    def recursive_call(self, pointer1, pointer2, pointer3=None):
        self.print_linked_list()
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


if __name__ == "__main__":
    # linked_list = LinkedList()
    # linked_list.insert_at_beginning(10)
    # linked_list.insert_at_beginning(100)
    # linked_list.insert_at_beginning(1000)
    # linked_list.append_element(0)
    # linked_list.append_list([1, 2, 3, 4, 5])
    # # 1000 --> 100 --> 10 --> 0 --> 1 --> 2 --> 3 --> 4 --> 5
    # linked_list.print_linked_list()
    #
    # print(linked_list.get_list_length())  # 9
    # linked_list.remove_element_at_index(2)
    # # 1000 --> 100 --> 0 --> 1 --> 2 --> 3 --> 4 --> 5
    # linked_list.print_linked_list()
    # linked_list.insert_element_at_index(3, 99)
    # # 1000 --> 100 --> 0 --> 99 --> x --> y --> z --> 1 --> 2 --> 3 --> 4 --> 5
    # linked_list.print_linked_list()
    # linked_list.insert_list_starting_index(4, ["x", "y", "z"])
    # # 100 --> 0 --> 99 --> x --> y --> z --> 1 --> 2 --> 3 --> 4 --> 5
    # linked_list.print_linked_list()
    # linked_list.remove_element_at_index(0)
    # # 100 --> 0 --> 99 --> x --> y --> z --> 1 --> 2 --> 3 --> 4 --> 5
    # linked_list.print_linked_list()
    # linked_list.insert_after_value("x", 9999999)
    # # 100 --> 0 --> 99 --> x --> 9999999 --> y --> z --> 1 --> 2 --> 3 --> 4 --> 5
    # linked_list.print_linked_list()
    # linked_list.remove_by_value("z")
    # # 100 --> 0 --> 99 --> x --> 9999999 --> y --> z --> 1 --> 2 --> 3 --> 4 --> 5
    # linked_list.print_linked_list()
    # print(f"tail value = {linked_list.get_tail().data}")
    # linked_list.contains_value(0)
    # linked_list.contains_value(10)
    # linked_list.contains_value(1100)
    # linked_list.contains_value('y')
    # linked_list.append_element(2)
    # linked_list.insert_at_beginning(2)
    # linked_list.insert_at_beginning(2)
    # linked_list.append_element(2)
    # linked_list.insert_element_at_index(4, 2)
    #
    # linked_list.print_linked_list()
    # # removing the first element of value 2
    # print("Removing the first element of value 2")
    # linked_list.remove_by_value(2)
    # linked_list.print_linked_list()
    # print("Removing all elements of value 2")
    # linked_list.remove_all_by_value(2)
    # linked_list.print_linked_list()
    # linked_list.reverse_linked_list()
    # print(f"Reversed linked list")
    # linked_list.print_linked_list()
    linked_list2 = LinkedList()
    linked_list2.insert_list_starting_index(0, [-10, 1, 3, 4, 8])
    linked_list2.print_linked_list()
    linked_list3 = LinkedList()
    linked_list3.insert_list_starting_index(0, [-1, 0, 2, 5])
    linked_list3.print_linked_list()
    linked_list2 = linked_list2.recursive_merge(linked_list3)
    # linked_list2 = linked_list2.merge_linked_lists(list_to_merge=linked_list3)
    linked_list2.print_linked_list()
