class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }
}

public class Main {

    public static void main(String args[]) {
        Node head = new Node(10);
        head.next = new Node(20);
        head.next.next = new Node(30);
        head.next.next.next = new Node(40);
        head.next.next.next.next = new Node(50);
        printlist(head);
        int pos=3;
        int x = 4;
        head = insertPos(head, pos, x);
        System.out.println();
        printlist(head);
    }

    public static void printlist(Node head) {
        Node curr = head;
        while (curr != null) {
            System.out.print(curr.data + " ");
            curr = curr.next;
        }
        System.out.println();
    }
    public static Node insertPos(Node head,int pos,int x){
        Node temp = new Node(x);
        if(pos==1){
            temp.next = head;
            return temp;
        }
        Node curr = head;
        for(int i =1 ; i<=pos-2 && curr!=null;i++){
            curr = curr.next;
        }
        if(curr == null) return head;
        temp.next = curr.next;
        curr.next = temp;
        return head;
    }
}
