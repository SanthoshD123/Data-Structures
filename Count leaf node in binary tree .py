class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_leaf_nodes(root):
    if not root:
        return 0

    queue = [root]
    leaf_count = 0

    while queue:
        node = queue.pop(0)
        if not node.left and not node.right:
            leaf_count += 1
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return leaf_count

# Example usage:
# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Leaf count:", count_leaf_nodes(root))  # Output: 3
