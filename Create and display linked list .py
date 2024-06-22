class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class sll:
    def __init__(self):
        self.head = None
    def display(self):
        temp = self.head
        if self.head is None:
            print("empty")
        while temp:
            print(temp.data,"-->",end="")
            temp = temp.next
L = sll()
n1= Node(10)
L.head = n1
n2 = Node(20)
L.head.next = n2
L.display()
