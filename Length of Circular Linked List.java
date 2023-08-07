class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }
}

public class Main {
    public static void main(String[] args) {
        Node head = new Node(10);
        head.next = new Node(20);
        head.next.next = new Node(30);
        head.next.next.next = new Node(40);
        head.next.next.next.next = head;
        int length = printCircular(head);
        System.out.println("Length of the circular linked list: " + length);
    }

    public static int printCircular(Node head) {
        if (head == null) return 0;
        int length = 1; 
        Node current = head.next;
        while (current != head) {
            length++;
            current = current.next;
        }
        System.out.print(head.data + " ");
        current = head.next;
        while (current != head) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        return length;
    }
}
