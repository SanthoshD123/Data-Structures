class Node{
    int data;
    Node next;
    Node(int x){
        data = x;
        next = null;
    }
}

public class Main
{
	public static void main(String[] args) {
		Node head = new Node(10);
		head.next = new Node(20);
		head.next.next = new Node(30);
		head.next.next.next = new Node(40);
		System.out.println("Original Linked List:");
    printLinkedList(head);
    head = reverse(head);
    System.out.println("\nReversed Linked List:");
    printLinkedList(head);
	}
	public static void printLinkedList(Node head){
	    Node curr = head;
	    while(curr != null){
	        System.out.print(curr.data+" ");
	        curr = curr.next;
	    }
	}
	public static Node reverse(Node head){
	    Node curr = head;
	    Node prev = null;
	    while(curr!=null){
	        Node next = curr.next;
	        curr.next = prev;
	        prev = curr;
	        curr = next;
	    }
	    return prev;
	}
	
}
