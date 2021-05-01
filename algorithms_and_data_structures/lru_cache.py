# implementation of LRU cache
# Delete the least recently used elements in the cache before storing any new values
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node
        self.previous = None


class DoublyLinkedList:
    def __init__(self, ):
        self.tail = None
        self.head = None

    def remove_tail(self):
        if not self.head:
            return "List is Empty"
        self.tail = self.tail.previous
        self.tail.next_node = None

    def set_head(self, node):
        if self.head == node:
            return
        elif not self.head:
            self.head = node
            self.tail = node
        elif self.head == self.tail:
            self.tail.previous = node
            self.head = node
            self.head.next_node = self.tail
        else:
            if self.tail == node:
                self.remove_tail()
            self.head.previous = node
            node.next_node = self.head
            self.head = node


class LRUCache:
    def __init__(self, maxsize):
        self.cache = {}
        self.maximum_size = maxsize
        self.current_size = 0
        self.most_recent = DoublyLinkedList()

    def get_value(self, key):
        """Given a key, the function returns the value associated with the key from the hash table"""
        if key not in self.cache:
            return None
        self.update_most_recent(self.cache[key])
        return self.cache[key].data

    def get_recently_used_key(self):
        return self.most_recent.head.key

    def insert_pair(self, key, value):
        if key not in self.cache:
            if self.current_size == self.maximum_size:
                self.remove_least_recent()
            else:
                self.current_size += 1
            self.cache[key] = Node(key, value)
        else:
            self.cache[key].data = value
        self.update_most_recent(self.cache[key])

    def remove_least_recent(self):
        key_to_remove = self.most_recent.tail.key
        self.most_recent.remove_tail()
        del self.cache[key_to_remove]

    def update_most_recent(self, node):
        self.most_recent.set_head = self.cache[node]
