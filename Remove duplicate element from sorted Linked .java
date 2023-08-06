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
		head.next = new Node(10);
		head.next.next = new Node(30);
		head.next.next.next = new Node(40);
        printLinkedList(head);
        System.out.println();
        Node removeDups = removeDups(head);
        printLinkedList(head);
	}
	public static void printLinkedList(Node head){
	    Node curr = head;
	    while(curr != null){
	        System.out.print(curr.data+" ");
	        curr = curr.next;
	    }
	}
	public static Node removeDups(Node head){
	    Node curr = head;
	    while(curr != null && curr.next != null){
	        if(curr.data == curr.next.data){
	            curr.next = curr.next.next;
	        }
	        else{
	            curr = curr.next;
	        }
	    }
	    return head;
	}
	
	
}
