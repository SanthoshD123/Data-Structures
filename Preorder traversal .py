def preorder_traversal(node):
    if node is not None:
        print(node.data, end=" ")
        preorder_traversal(node.left)
        preorder_traversal(node.right)

# Example usage (using the same tree as above):
print("\nPreorder traversal of binary tree:")
preorder_traversal(root)
