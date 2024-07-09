class Node:
    def __init__(self, val1, val2=None):
        self.val1 = val1
        self.val2 = val2
        self.left = None
        self.middle = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.val1:
            if node.left:
                self._add(val, node.left)
            else:
                node.left = Node(val)
        elif val > node.val1:
            if node.right:
                self._add(val, node.right)
            else:
                node.right = Node(val)
        elif node.val2 is None or val == node.val2:
            if node.middle:
                self._add(val, node.middle)
            else:
                node.middle = Node(val)

    def find(self, val):
        if self.root:
            return self._find(val, self.root)

    def _find(self, val, node):
        if val == node.val1:
            return node
        elif val < node.val1 and node.left:
            return self._find(val, node.left)
        elif val > node.val1 and (node.val2 is None or val < node.val2) and node.middle:
            return self._find(val, node.middle)
        elif val > node.val1 and node.val2 is not None and val == node.val2 and node.right:
            return self._find(val, node.right)

    def delete_tree(self):
        # Garbage collector will do this for us.
        if self.root:
            self.root = None

    def view_tree(self):
        if self.root:
            self._view_tree(self.root)

    def _view_tree(self, node):
        if node:
            self._view_tree(node.left)
            print(node.val1, end=" ")
            if node.val2 is not None:
                print(node.val2, end=" ")
            self._view_tree(node.middle)
            self._view_tree(node.right)

# Example usage:
tree = Tree()
tree.add(3)
tree.add(4)
tree.add(0)
tree.add(8)
tree.add(2)

print("Tree structure:")
tree.view_tree()

found_node = tree.find(3)
if found_node:
    print(f"\nFound node with value 3: {found_node.val1}")
else:
    print("\nNode with value 3 not found")

not_found_node = tree.find(10)
if not_found_node:
    print(f"Found node with value 10: {not_found_node.val1}")
else:
    print("Node with value 10 not found")

# Clean up
tree.delete_tree()
