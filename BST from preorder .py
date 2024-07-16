class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert_into_bst(root.left, val)
    else:
        root.right = insert_into_bst(root.right, val)
    return root

def bst_from_preorder(preorder):
    if not preorder:
        return None
    root = TreeNode(preorder[0])
    for value in preorder[1:]:
        insert_into_bst(root, value)
    return root

# Function to print the tree in inorder for verification
def inorder_traversal(root):
    if not root:
        return []
    return inorder_traversal(root.left) + [root.val] + inorder_traversal(root.right)

# Example usage
preorder = [8, 5, 1, 7, 10, 12]
root = bst_from_preorder(preorder)
print("Inorder traversal of the constructed BST:", inorder_traversal(root))
