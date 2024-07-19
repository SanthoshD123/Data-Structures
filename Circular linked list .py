class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        nodes = []
        if self.head:
            temp = self.head
            while True:
                nodes.append(temp.data)
                temp = temp.next
                if temp == self.head:
                    break
        return nodes

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node

    def remove(self, key):
        if self.head:
            if self.head.data == key:
                if self.head.next == self.head:
                    self.head = None
                else:
                    temp = self.head
                    while temp.next != self.head:
                        temp = temp.next
                    temp.next = self.head.next
                    self.head = self.head.next
            else:
                prev = None
                temp = self.head
                while temp.next != self.head:
                    prev = temp
                    temp = temp.next
                    if temp.data == key:
                        prev.next = temp.next
                        break

# Example usage
cll = CircularLinkedList()
cll.append(1)
cll.append(2)
cll.append(3)
print("Display:", cll.display())  # Output: [1, 2, 3]

cll.prepend(0)
print("Display after prepend:", cll.display())  # Output: [0, 1, 2, 3]

cll.remove(2)
print("Display after remove:", cll.display())  # Output: [0, 1, 3]
