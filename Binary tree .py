class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.value = val

class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.value:
            if node.left:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self, val):
        if self.root:
            return self._find(val, self.root)

    def _find(self, val, node):
        if val == node.value:
            return node
        elif val < node.value and node.left:
            return self._find(val, node.left)
        elif val > node.value and node.right:
            return self._find(val, node.right)

# Example usage
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)

# View the tree
print("Inorder traversal of the tree:")
tree.view_tree()
