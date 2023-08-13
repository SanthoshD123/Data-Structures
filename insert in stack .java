import java.util.Stack;

public class Main
{
	public static void main(String[] args) {
		int []arr = {1,2,3,4,5};
		int n = arr.length;
		
		Stack<Integer> s = new Stack<>();
		for(int i=0;i<n;i++){
		    s.push(arr[i]);
		}
		while(!s.isEmpty()){
		    System.out.print(s.pop()+" ");
		}
	}
}
