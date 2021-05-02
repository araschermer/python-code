class TreeNode:
    def __init__(self, data):
        self.data = data
        # since this is a general tree, the number of children nodes is unlimited
        self.children = [] # a list doesn't prevent duplicates
        self.parent = None

    def add_node(self, node):
        node.parent = self  #
        self.children.append(node)

    def print_tree(self):
        level = self.get_level()
        level = "  ―| " * level
        print(f"{level}{self.data}")
        for child_node in self.children:
            child_node.print_tree()
        # another way  to print the tree without recursion:
        # for child in self.children:
        #     print(child.data)
        #     # print("Nested nodes:")
        #     for node in child.children:
        #         print(f"   {node}")

    def get_level(self):
        level = 0
        node_parent = self.parent
        while node_parent:
            node_parent = node_parent.parent
            level += 1
        return level


def build_tree():
    root = TreeNode("Root")
    child = TreeNode("Child1")
    child2 = TreeNode("Child2")
    child3 = TreeNode("Child3")
    child4 = TreeNode("Child4")
    child.add_node(TreeNode("child11"))
    child.add_node(TreeNode("child12"))
    child.add_node(TreeNode("child13"))
    child.add_node(TreeNode("child14"))
    child2.add_node(TreeNode("child21"))
    child3.add_node(TreeNode("child31"))
    root.add_node(child)
    root.add_node(child2)
    root.add_node(child3)
    root.add_node(child4)

    return root


if __name__ == "__main__":
    tree = build_tree()
    tree.print_tree()
