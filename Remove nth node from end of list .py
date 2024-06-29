class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, N):
    dummy = ListNode(0)
    dummy.next = head
    slowPtr, fastPtr = dummy, dummy

    # Move fastPtr N steps ahead
    for _ in range(N + 1):
        fastPtr = fastPtr.next

    # Move both pointers until fastPtr reaches the end
    while fastPtr:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next

    # Remove the Nth node
    slowPtr.next = slowPtr.next.next

    return dummy.next

# Example usage
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

n = 2
new_head = removeNthFromEnd(head, n)

# Display the modified linked list
while new_head:
    print(new_head.val, end=" ")
    new_head = new_head.next
