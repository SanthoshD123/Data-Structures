import java.util.*;

public class Main
{
	public static void main(String[] args) {
		int []arr = {10,20,20,30,40,50,40};
		System.out.print(countDistinct(arr));
	}
	public static int countDistinct(int arr[]){
	    HashSet<Integer> s = new HashSet<>();
	    for(int i=0;i<arr.length;i++){
	        s.add(arr[i]);
	    }
	    return s.size();
	}
}
