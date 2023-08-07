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
		head.next.next.next.next = head;
		printCircular(head);
	}
	public static void printCircular(Node head){
	    if(head==null)return;
	    System.out.print(head.data+" ");
	    for(Node i=head.next; i!=head; i=i.next){
	        System.out.print(i.data+" ");
	    }
	}
}
