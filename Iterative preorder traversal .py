class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def iterative_preorder_traversal(root):
    if not root:
        return
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        print(node.value, end=' ')
        
        # Push right child first so that left is processed first
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Example usage:
# Constructing the binary tree
#         1
#        / \
#       2   3
#      / \   \
#     4   5   6

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

iterative_preorder_traversal(root)
