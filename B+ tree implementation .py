class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf
        self.next_leaf = None

class BPlusTree:
    def __init__(self, degree):
        self.root = BPlusTreeNode(leaf=True)
        self.degree = degree

    def insert(self, key):
        if key in self.search(key):
            return
        
        if len(self.root.keys) == 2 * self.degree - 1:
            new_root = BPlusTreeNode()
            new_root.children.append(self.root)
            self.split_child(new_root, 0)
            self.root = new_root

        self.insert_non_full(self.root, key)

    def insert_non_full(self, node, key):
        index = len(node.keys) - 1
        if node.leaf:
            node.keys.append(None)
            while index >= 0 and key < node.keys[index]:
                node.keys[index + 1] = node.keys[index]
                index -= 1
            node.keys[index + 1] = key
        else:
            while index >= 0 and key < node.keys[index]:
                index -= 1
            index += 1
            if len(node.children[index].keys) == 2 * self.degree - 1:
                self.split_child(node, index)
                if key > node.keys[index]:
                    index += 1
            self.insert_non_full(node.children[index], key)

    def split_child(self, parent, index):
        degree = self.degree
        child = parent.children[index]
        new_child = BPlusTreeNode(leaf=child.leaf)

        parent.keys.insert(index, child.keys[degree - 1])
        parent.children.insert(index + 1, new_child)

        new_child.keys = child.keys[degree:2 * degree - 1]
        child.keys = child.keys[0:degree - 1]

        if not child.leaf:
            new_child.children = child.children[degree:2 * degree]
            child.children = child.children[0:degree - 1]

    def search(self, key, node=None):
        if node is None:
            node = self.root

        index = 0
        while index < len(node.keys) and key > node.keys[index]:
            index += 1

        if index < len(node.keys) and key == node.keys[index]:
            return node

        if node.leaf:
            return None

        return self.search(key, node.children[index])

    def traverse(self):
        node = self.root
        while not node.leaf:
            node = node.children[0]
        while node:
            for key in node.keys:
                print(key, end=' ')
            node = node.next_leaf
        print()

# Example usage:
if __name__ == "__main__":
    b_plus_tree = BPlusTree(degree=3)
    keys = [3, 7, 1, 4, 2, 9, 10, 5, 8, 6]
    
    for key in keys:
        b_plus_tree.insert(key)
    
    print("Traversal of constructed B+ tree:")
    b_plus_tree.traverse()
    
    search_key = 5
    result = b_plus_tree.search(search_key)
    if result:
        print(f"Key {search_key} found in the tree.")
    else:
        print(f"Key {search_key} not found in the tree.")
