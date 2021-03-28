class BinaryTree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def insert(self, data):
        # if data is self.data:
        #     return  # if tree doesn't store duplicates
        if data <= self.data:
            if self.left is not None:
                self.left.insert(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right is not None:
                self.right.insert(data)
            else:
                self.right = BinaryTree(data)

    def print_inorder(self):
        """prints the tree nodes in order traversal, starting from the left node-children,
         then the root, followed by the right node-children. """
        elements = []
        if self.left:
            elements += self.left.print_inorder()
        elements.append(self.data)
        if self.right:
            elements += self.right.print_inorder()
        print(elements)

        return elements

    def print_postorder(self):
        """prints the tree nodes post-order traversal, starting from the left node-children,
         followed by the right node-children, and eventually  the root """
        elements = []
        if self.left:
            elements += self.left.print_postorder()
        if self.right:
            elements += self.right.print_postorder()
        elements.append(self.data)
        print(elements)

        return elements

    def print_preorder(self):
        """prints the tree nodes post-order traversal, starting with the root, then the left node-children,
         followed by the right node-children."""
        elements = [self.data]
        if self.left:
            elements += self.left.print_preorder()
        if self.right:
            elements += self.right.print_preorder()
        print(elements)
        return elements

    def get_max(self):
        """returns the maximum node value in the tree"""
        if self.right is None:
            return self.data
        return self.right.get_max()

    def get_min(self):
        """returns the minimum node value in the tree"""
        if self.left is None:
            return self.data
        return self.left.get_min()

    def calculate_sum(self, root):
        """returns the sum of the integers in the tree"""
        if root is None:
            return 0
        return root.data + self.calculate_sum(root.left) + self.calculate_sum(root.right)

    def contains(self, data):
        """return True if the tree contains the given key """
        if self.data == data:
            return True

        if data < self.data:
            if self.left:
                return self.left.contains(data)
            else:
                return False

        if data > self.data:
            if self.right:
                return self.right.contains(data)
            else:
                return False

    def delete(self, key):
        """deleted the given key from the tree, and replaces it with data minimum value in its right sub-tree"""
        if key < self.data:
            if self.left:
                self.left = self.left.delete(key)
        elif key > self.data:
            if self.right:
                self.right = self.right.delete(key)
        else:
            if self.left is None and self.right is None:
                return None
            elif self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            successor = self.right.get_min()
            print("successor = ", successor)
            self.data = successor
            self.right = self.right.delete(successor)
        return self


def build_tree(elements):
    """Builds a tree from a given list of elements. and returns the root node."""
    root = BinaryTree(elements[0])
    for i in range(1, len(elements)):
        root.insert(elements[i])

    return root


if __name__ == '__main__':
    # binary_tree1 = build_tree([99, 60, 20, 1, 0, 87, 39])
    # binary_tree2 = build_tree([99, 60, 20, 1, 100, 87, 39])
    # print(binary_tree1.contains(39))  # True
    # print(binary_tree1.contains(990))  # False
    # print("Preorder1")
    # binary_tree1.print_preorder()
    # #   99
    # #  |    |
    # #  60   87
    # # |  |
    # # 20 39
    # # |
    # # 1
    # # |
    # # 0
    # # should output  [99, 60, 20, 1, 0, 39, 87] for an input of  [99, 60, 20, 1, 0, 87, 39]
    # binary_tree2.print_preorder()
    # #  and  for
    # #   99
    # #  |    |
    # #  60   100
    # # |  |
    # # 20 39
    # # |   |
    # # 1    87
    # # should output  [99, 60, 20, 1, 39, 87, 100] for an input of  [99, 60, 20, 1, 100, 87, 39]
    #
    # binary_tree1.print_postorder()
    # # binary_tree1.print_inorder()
    # # print(
    # #     binary_tree1.find_min(),
    # #     binary_tree1.find_max(),
    # #     binary_tree2.find_min(),
    # #     binary_tree2.find_max())
    # print("delete 20")
    # binary_tree1.delete(20)
    # #   99
    # #  |    |
    # #  60   87
    # # |  |
    # # 0 39
    # # |
    # # 1
    ## binary_tree1.print_preorder()
    binary_tree3 = build_tree([1, 42, 10, 20, 9, 29, 50, 14])
    # binary_tree3.print_preorder()
    # binary_tree3.delete(9)
    # binary_tree3.print_preorder()
    # [19, 10, 42, 20, 29, 34, 50]
    # binary_tree3.delete(200)
    binary_tree3.print_preorder()
    # [1, 42, 10, 9, 20, 14, 29, 50]
    binary_tree3.delete(42)
    binary_tree3.delete(10)
    # binary_tree3.delete(20)
    # binary_tree3.deleteNode(10)
    binary_tree3.print_preorder()
