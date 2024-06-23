class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class sll:
    def __init__(self):
        self.head = None

    def insertion_beginning(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb

    def insertion_end(self,data):
        ne = Node(data)
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ne

    def insertion_position(self,pos,data):
        np = Node(data)
        temp = self.head
        for i in range(pos-1):
            temp = temp.next
        np.data = data
        np.next = temp.next
        temp.next = np

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
L.insertion_beginning(5)
L.insertion_end(30)
L.insertion_position(3,25)
L.display()
