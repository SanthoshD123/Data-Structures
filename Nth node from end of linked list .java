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
        printLinkedList(head);
        int n=2;
        Node nthNode = nthNode(head, n);
        System.out.println("\nNth Node from the end: " + nthNode.data);
	}
	public static void printLinkedList(Node head){
	    Node curr = head;
	    while(curr != null){
	        System.out.print(curr.data+" ");
	        curr = curr.next;
	    }
	}
	public static Node nthNode(Node head,int n){
	    if(head==null) return null;
	    Node first= head;
	    for(int i=0;i<n;i++){
	        if(first==null)return null;
	        first= first.next;
	    }
	    Node second = head;
	    while(first!=null){
	        second = second.next;
	        first = first.next;
	    }
	    return second;
	}
	
	
}
