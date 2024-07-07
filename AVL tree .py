class Node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 1  # Height of the node (max distance to leaf)

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, root, value):
        if not root:
            return Node(value)
        if value < root.value:
            root.left_child = self.insert(root.left_child, value)
        else:
            root.right_child = self.insert(root.right_child, value)

        root.height = 1 + max(self.get_height(root.left_child), self.get_height(root.right_child))
        balance = self.get_balance(root)

        # Perform rotations if necessary
        if balance > 1:
            if value < root.left_child.value:
                return self.right_rotate(root)
            else:
                root.left_child = self.left_rotate(root.left_child)
                return self.right_rotate(root)
        if balance < -1:
            if value > root.right_child.value:
                return self.left_rotate(root)
            else:
                root.right_child = self.right_rotate(root.right_child)
                return self.left_rotate(root)

        return root

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left_child) - self.get_height(node.right_child)

    def left_rotate(self, z):
        y = z.right_child
        T2 = y.left_child

        y.left_child = z
        z.right_child = T2

        z.height = 1 + max(self.get_height(z.left_child), self.get_height(z.right_child))
        y.height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))

        return y

    def right_rotate(self, y):
        z = y.left_child
        T3 = z.right_child

        z.right_child = y
        y.left_child = T3

        y.height = 1 + max(self.get_height(y.left_child), self.get_height(y.right_child))
        z.height = 1 + max(self.get_height(z.left_child), self.get_height(z.right_child))

        return z

# Example usage
if __name__ == "__main__":
    avl_tree = AVLTree()
    values = [10, 20, 30, 40, 50, 25]
    for value in values:
        avl_tree.root = avl_tree.insert(avl_tree.root, value)
