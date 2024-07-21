class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_duplicates(head):
    current = head
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
    return head

# Helper function to create a linked list from a list of values
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Example usage:
lst = [1, 1, 2, 3, 3, 4, 4, 5]
head = create_linked_list(lst)
print("Original list:")
print_linked_list(head)

head = remove_duplicates(head)
print("List after removing duplicates:")
print_linked_list(head)
